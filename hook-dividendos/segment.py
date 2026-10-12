# Uso: python3 segment.py <carpeta_trabajo> [frames_de_corte separados por coma, base 0]
#   lee <carpeta>/src/*.png y <carpeta>/selfie_multiclass.tflite, escribe <carpeta>/masks/*.png
import sys,glob,os,numpy as np,cv2,mediapipe as mp
from mediapipe.tasks.python import vision, BaseOptions
S=sys.argv[1]
CUTS={int(c) for c in sys.argv[2].split(',')} if len(sys.argv)>2 else set()
os.makedirs(S+'/masks',exist_ok=True)
seg=vision.ImageSegmenter.create_from_options(vision.ImageSegmenterOptions(base_options=BaseOptions(model_asset_path=S+'/selfie_multiclass.tflite'),running_mode=vision.RunningMode.VIDEO,output_confidence_masks=True))
prev=None
files=sorted(glob.glob(S+'/src/*.png'))
for i,f in enumerate(files):
    bgr=cv2.imread(f); rgb=cv2.cvtColor(bgr,cv2.COLOR_BGR2RGB)
    r=seg.segment_for_video(mp.Image(image_format=mp.ImageFormat.SRGB,data=rgb),int(i*1000/30))
    m=1-r.confidence_masks[0].numpy_view()  # 0 = background
    m=cv2.resize(m,(1080,1920),interpolation=cv2.INTER_LINEAR)
    # refine edges with guided-like filter on luminance
    m=np.clip((m-0.35)/0.3,0,1).astype(np.float32)
    n,lab,st,_=cv2.connectedComponentsWithStats((m>0.5).astype(np.uint8),8)
    if n>1:
        big=1+int(np.argmax(st[1:,cv2.CC_STAT_AREA]))
        keep=(lab==big).astype(np.uint8)
        keep=cv2.dilate(keep,np.ones((25,25),np.uint8))
        m=m*keep
    if prev is not None and i not in CUTS: m=0.6*m+0.4*prev
    prev=m
    m2=cv2.GaussianBlur(m,(0,0),1.5)
    cv2.imwrite(S+'/masks/'+os.path.basename(f),(m2*255).astype(np.uint8))
print('done',len(files))
