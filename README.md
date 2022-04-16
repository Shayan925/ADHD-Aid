# Lyon Hacks II (April 15-17th, 2022)

## Inspiration 
- Our team personally had a classmate with ADHD, and he struggled with online learning due to being unable to remain focused for extended periods of time. 
- This inspired our team to create a software to support him and others with attention problems/disabilities 

## What it does 
- The ADHD aid is a software application used to help those with Attention Deficit Hyperactivity Disorder. By tracking the user's eyes, the ADHD aid sends a visual/audio queue to focus the individual upon facing distraction. 
- Our software can also be used by teachers as an anti-cheat for online learning. This is due to the fact that the ADHD aid keeps a record of the time as well as the duration that the user looks away from the monitor. 

## How we built it 
- Utilized the MediaPipe framework to build a machine learning pipeline for detecting and tracking any person's irises and the direction they are facing. 
- OpenCV was used to get video-input from the camera and draw overlays on top such as text, lines, and shapes. 
- The Numpy library helped with processing large amounts of number values that were received from the face mesh created with MediaPipe and converted into coordinates to be plotted on top of the video. - Additionally, the winsound library was used to play the audio file when the user lost focus for too long. 

## Challenges we ran into 
- Detecting the eyes and iris was not too difficult, but determining whether the irises are looking to the right, left, or center is where the real challenge was. We overcame it by finding a non-moving reference point and calculating the horizontal and vertical distance away from the center of the iris, to figure out the direction it is moving in. 

## Accomplishments that we're proud of 
- Since we personally knew many who struggled with online learning, and paying attention, we are extremely proud that our project can support those with attention issues. 

## What we learned 
- We learned the difficulties in creating a functional iris tracker, but through perseverance, we successfully gained the knowledge to create software revolving around it. 

## What's next for ADHD Aid 
- Our team aims to implement connections with video services like google meets/zoom calls to finalize the program.
- Also a notification system to inform the supervisor(s) whether it be to help a child with a disability or to catch cheaters.
