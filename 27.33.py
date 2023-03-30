# Bowling involves 10 frames. Each frame starts with 10 pins. The bowler has two throws to knock all 10 pins down. The total score is the sum of pins knocked down, with some special rules.
#
# For the first 9 frames:
#
# If all 10 pins are knocked down on a frame's first throw (a "strike"), that frame's score is the previous frame plus 10 plus the next two throws. (No second throw is taken).
#
# If all 10 pins are knocked down after a frame's second throw (a "spare"), that frame's score is the previous frame plus 10 plus the next throw.
#
# In the 10th frame, if the bowler's first throw is a strike, or the first two throws yields a spare, the bowler gets a third throw. The 10th frame's score is the previous frame's score plus the pins knocked down in the 10th frame's two or three throws.
#
# Given integers represents all throws for a game, output on one line each frame's score followed by a space (and end with a newline). Note that the number of throws may be as few as 11 (strikes in first 9 frames, and no strike/spare in 10th frame), or as many as 21 (2 throws in first 9 frames, then 3 in 10th).
#
# For simplicity, the input will always have 21 integers. If the game ended with fewer than 21 throws, the remaining integers will be 0's and can be ignored.
#
# Ex: A perfect game is one where every throw is a strike. The 21 input integers will be: 10 10 10 10 10 10 10 10 10 10 10 10. The output will be: 30 60 90 120 150 180 210 240 270 300.
#
# Hints:
#
# A first for loop should just read in the 21 scores in the first vector.
# A second for loop should fill the second vector's first 9 elements (first 9 frames).
# Additional code should compute the 10th frame, which is unique.

# * COME BACK TO THIS ONE AND ITS LGOIC

throwValues = [0]*21
frameScores = [0]*10
t = 0 # Throw index
f = 0 # Frame index
frameScore = 0

# Read in the 21 possible throw values for the 10 frames
for t in range(21):
    throwValues[t] = int(input())

# Compute score of each of first 9 frames
t = 0
for f in range(9):
    frameScore = 0
    frameScore = throwValues[t] # Add first throw of this frame
    if frameScore == 10: # Strike
        frameScore += throwValues[t + 1] + throwValues[t + 2] # Add next two throws
    else: # Not a strike
        t += 1
        frameScore += throwValues[t] # Add second throw of this frame
        if frameScore == 10: # Spare
            frameScore += throwValues[t + 1] # Add next throw
    t += 1
    if f > 0: # Not first frame, so add previous frame's score
        frameScore += frameScores[f - 1] # Add previous frame's score
    frameScores[f] = frameScore

# 10th frame
frameScores[f] = frameScores[f - 1] + throwValues[t] + throwValues[t + 1] + throwValues[t + 2]
# Note: If only two throws in 10th frame, the t+2 value will be 0, so OK to add. Keeps code simpler.

# Note that above, frame 1 is at element 0, frame 2 at element 1, ..., and frame 10 at element 9.

for f in range(10):
    print(frameScores[f], end=" ")
print()

