# This Is A Collection Of Basic / Often Used Math Functions
# We Already Have A Set Of Basic / Often Used String Methods So Now It's Time We Do The Same For Math Operations

import math  # Importing Math Library So We Can Use Some Math Functions Located In That Library

# If You Want To Learn More About This Import Statement Check The Module Section For More Details

# Rounds A Value To An Integer By Default Unless You Specify The Number Of Decimal Places You Want To Round To
print(round(7.496283, 2))

# This Will Round The Number "Up" To The Next Integer
print(math.ceil(7.000000001))

# This Will Round The Number "Down" To The Next Integer
print(math.floor(7.999999999999999))

print(abs(-12.57))  # Returns The Absolute Value Of A Number (Positive)

print(pow(2, 6))  # Returns The Exponential Like 2⁶ | 2 * 2 * 2 * 2 * 2 * 2

print(math.sqrt(9))  # Returns The Square Root Of A Number As An Float

# Returns The Highest Value Of A Collection Of Numbers
print(max(1, 2, 3, 4, 5))

print(min(1, 2, 3, 4, 5))  # Returns The Lowest Value Of A Collection Of Numbers
