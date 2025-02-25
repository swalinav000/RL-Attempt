# Mock-up of code sections

# Imports
import keras
import tensorflow

# Data set contains 
# [ (height, inertia, motor on/off) ] 

# States
## Extend Airbrakes [in a gradient]
## Retract Airbrakes [in a gradient]

# Rewards
## If target height - current height diff is expected to reach w current inertia - drag 
## +++ reward
## If you're going to overshoot then
## --- reward
## else 
## 000 reward

# Observations 
## Inertia at time
## Height at time 
## Airbrake motor state
