# Python evm
 An easy to use Python API for EVM (Eulerian Video Magnification). Also known as motion magnification.
 <div align="center">
  <img src="data/mm_baby.gif">
</div>
 
 Eulerian motion magnification works by spatially decomposing individual frames and temporally filtering the video.
 Introduced in Eulerian Video Magnification for Revealing Subtle Changes in the World by Hao-Yu Wu and Michael Rubinstein and Eugene Shih and John Guttag and Fr\'{e}do Durand and
 William T. Freeman.
 
 Original matlab code from http://people.csail.mit.edu/mrub/evm/
 
 ### Usage
 A simple example of loading a video, magnifying it and saving it.
 ```python
import py_evm
video = load_video("data/baby.mp4")
mm_video = magnify(video)
save_video(mm_video, "mm_baby")
```
Do it all in one line.
 ```python
import py_evm
magnify("data/baby.mp4")
```
Change the parameters and use the motion magnified video in down stream tasks such as video analysis using neural networks.
 ```python
import py_evm
video = load_video("data/baby.mp4")
mm_video = magnify(video, alpha=30, r1=0.4, r2=0.04)
.
.
.
model(mm_video)
```

### Future improvements
- Currently only supports ideal pass filtering, add others.
- Differentiable version using pytorch GPU
- Fast linearized version
