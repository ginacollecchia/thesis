#The Pitch Class Profile system assigns the integers 0 through 11 to the
#12 pitches in 1 octave:

#C=0
#C#=1
#D=2
#D#=3
#E=4
#F=5
#F#=6
#G=7
#G#=8
#A=9
#A#=10
#B=11

#major keys=0 thru 11, minor keys=12 thru 23
for j in range(0,24):
	key.append(j)

#query "What is the key in pitch class value, where 0 through 11 denote the #major keys C through B major, and 12 through 23 denote the minor keys C #through B minor?"; j

#The root of a chord is its Roman numeral plus the PCP of the key j,
#mod 12; the third is either 3 or 4 PCP's away from the root; the
#fifth is either 6, 7, or 8; and the seventh is either 9, 10, or 11.
#When there is not a seventh specified, the fourth and fifth entry of
#the distinct row vector defining the Roman numeral name are -1, i.e.,
#not a PCP. When a seventh is specified, it can either be a minor or 
#major third away from the fifth (3 or 4 PCP's away), except in the case
#of an augmented seventh chord, which can only have a seventh 3 PCP's
#from its fifth. For augmented seventh chords, the fifth entry of their
#Roman numeral's row vector is -1, and for all other seventh chords,
#all entries are nonnegative.

I=[(0+key[j])%12, (4+key[j])%12, (7+key[j])%12, -1, -1]

Isev=[(0+key[j])%12, (4+key[j])%12, (7+key[j])%12, (10+key[j])%12, (11+key[j])%12]

Iaug=[(0+key[j])%12, (4+key[j])%12, (8+key[j])%12, -1, -1]

Iaugsev=[(0+key[j])%12, (4+key[j])%12, (8+key[j])%12, (11+key[j])%12, -1]

littlei=[(0+key[j])%12, (3+key[j])%12, (7+key[j])%12, -1, -1]

littleisev=[(0+key[j])%12, (3+key[j])%12, (7+key[j])%12, (10+key[j])%12, (11+key[j])%12]

bii=[(1+key[j])%12, (5+key[j])%12, (8+key[j])%12, -1, -1]

biisev=[(1+key[j])%12, (5+key[j])%12, (8+key[j])%12, (11+key[j])%12, (0+key[j])%12]

littleii=[(2+key[j])%12, (5+key[j])%12, (9+key[j])%12, -1, -1]

littleiisev=[(2+key[j])%12, (5+key[j])%12, (9+key[j])%12, (0+key[j])%12, (1+key[j])%12]

iidim=[(2+key[j])%12, (5+key[j])%12, (8+key[j])%12, -1,-1]

iidimsev=[(2+key[j])%12, (5+key[j])%12, (8+key[j])%12, (11+key[j])%12, (0+key[j])%12]

III=[(3+key[j])%12, (7+key[j])%12, (10+key[j])%12, -1, -1]

IIIsev=[(3+key[j])%12, (7+key[j])%12, (10+key[j])%12, (1+key[j])%12, (2+key[j])%12]

IIIaug=[(3+key[j])%12, (7+key[j])%12, (11+key[j])%12, -1, -1]

IIIaugsev=[(3+key[j])%12, (7+key[j])%12, (11+key[j])%12, (2+key[j])%12, -1]

littleiii=[(4+key[j])%12, (7+key[j])%12, (11+key[j])%12, -1, -1]

littleiiisev=[(4+key[j])%12, (7+key[j])%12, (11+key[j])%12, (2+key[j])%12, (3+key[j])%12]

IV=[(5+key[j])%12, (9+key[j])%12, (0+key[j])%12, -1, -1]

IVsev=[[(5+key[j])%12, (9+key[j])%12, (0+key[j])%12, (3+key[j])%12, (4+key[j])%12]

IVaug=[(5+key[j])%12, (9+key[j])%12, (1+key[j])%12, -1, -1]

IVaugsev=[(5+key[j])%12, (9+key[j])%12, (1+key[j])%12, (4+key[j])%12, -1]

littleiv=[(5+key[j])%12, (8+key[j])%12, (0+key[j])%12, -1, -1]

littleivsev=IVsev=[[(5+key[j])%12, (8+key[j])%12, (0+key[j])%12, (3+key[j])%12, (4+key[j])%12]

V=[(7+key[j])%12, (11+key[j])%12, (2+key[j])%12, -1, -1]

Vsev=[(7+key[j])%12, (11+key[j])%12, (2+key[j])%12, (5+key[j])%12, (6+key[j])%12)]

Vaug=[(7+key[j])%12, (11+key[j])%12, (3+key[j])%12, -1, -1]

Vaugsev=[(7+key[j])%12, (11+key[j])%12, (3+key[j])%12, (6+key[j])%12, -1]

littlev=[(7+key[j])%12, (10+key[j])%12, (2+key[j])%12, -1, -1]

littlevsev=[(7+key[j])%12, (10+key[j])%12, (2+key[j])%12, (5+key[j])%12, (6+key[j])%12)]

VI=[(8+key[j])%12, (0+key[j])%12, (3+key[j])%12, -1, -1]

VIsev=[(8+key[j])%12, (0+key[j])%12, (3+key[j])%12, (6+key[j])%12, (7+key[j])%12]

VIaug=[(8+key[j])%12, (0+key[j])%12, (4+key[j])%12, -1, -1]

VIaugsev=[(8+key[j])%12, (0+key[j])%12, (4+key[j])%12, (7+key[j])%12, -1]

littlevi=[(9+key[j])%12, (0+key[j])%12, (4+key[j])%12, -1, -1]

littlevisev=[(9+key[j])%12, (0+key[j])%12, (4+key[j])%12, (7+key[j])%12, (8+key[j])%12]

VII=[(10+key[j])%12, (2+key[j])%12, (5+key[j])%12, -1, -1]

VIIsev=[(10+key[j])%12, (2+key[j])%12, (5+key[j])%12, (8+key[j])%12, (9+key[j])%12]

VIIaug=[(10+key[j])%12, (2+key[j])%12, (6+key[j])%12, -1, -1]

VIIaugsev=[(10+key[j])%12, (2+key[j])%12, (6+key[j])%12, (9+key[j])%12, -1]

viidim=[(11+key[j])%12, (2+key[j])%12, (5+key[j])%12, -1,-1]

viidimsev=[(11+key[j])%12, (2+key[j])%12, (5+key[j])%12, (8+key[j])%12, (9+key[j])%12]

VofV=[(2+key[j])%12, (6+key[j])%12, (9+key[j])%12, -1,-1]

VofVsev=[(2+key[j])%12, (6+key[j])%12, (9+key[j])%12, (0+key[j])%12, (1+key[j])%12]

littlevofV=[(2+key[j])%12, (5+key[j])%12, (9+key[j])%12, -1,-1]

littlevofVsev=[(2+key[j])%12, (5+key[j])%12, (9+key[j])%12, (0+key[j])%12, (1+key[j])%12]

Vofvi=[(4+key[j])%12, (8+key[j])%12, (11+key[j])%12, -1,-1]

Vofvisev=[(4+key[j])%12, (8+key[j])%12, (11+key[j])%12, (2+key[j])%12, (3+key[j])%12]

Vofiii=[(11+key[j])%12, (3+key[j])%12, (6+key[j])%12, -1, -1]

Vofiiisev=[(11+key[j])%12, (3+key[j])%12, (6+key[j])%12, (9+key[j])%12, (10+key[j])%12]

Vofii=[(9+key[j])%12, (1+key[j])%12, (4+key[j])%12, -1, -1]

Vofiisev=[(9+key[j])%12, (1+key[j])%12, (4+key[j])%12, (7+key[j])%12, (8+key[j])%12]

Vofviidim=[(6+key[j])%12, (10+key[j])%12, (1+key[j])%12, -1, -1]

Vofviidimsev=[(6+key[j])%12, (10+key[j])%12, (1+key[j])%12, (4+key[j])%12, (5+key[j])%12]

viidimofV=[(6+key[j])%12, (9+key[j])%12, (0+key[j])%12, -1, -1]

viidimofVsev=[(6+key[j])%12, (9+key[j])%12, (0+key[j])%12, (3+key[j])%12, (4+key[j])%12]

viidimofii=[(1+key[j])%12, (4+key[j])%12, (7+key[j])%12, -1, -1]

viidimofiisev=[(1+key[j])%12, (4+key[j])%12, (7+key[j])%12, (10+key[j])%12, (11+key[j])%12]

viidimofIV=[(5+key[j])%12, (8+key[j])%12, (11+key[j])%12, -1, -1]

viidimofIVsev=[(5+key[j])%12, (8+key[j])%12, (11+key[j])%12, (2+key[j])%12, (3+key[j])%12]

viidimofbII=[(0+key[j])%12, (3+key[j])%12, (6+key[j])%12, -1, -1]

viidimofbIIsev=[(0+key[j])%12, (3+key[j])%12, (6+key[j])%12, (9+key[j])%12, (10+key[j])%12]

viidimofiii=[(3+key[j])%12, (6+key[j])%12, (9+key[j])%12, -1, -1]

viidimofiiisev=[(3+key[j])%12, (6+key[j])%12, (9+key[j])%12, (0+key[j])%12, (1+key[j])%12]

littlevofiii=[(11+key[j])%12, (2+key[j])%12, (6+key[j])%12, -1, -1]

littlevofiiisev=[(11+key[j])%12, (2+key[j])%12, (6+key[j])%12, (9+key[j])%12, (10+key[j])%12]

ivofiv=[(10+key[j])%12, (1+key[j])%12, (5+key[j])%12, -1, -1]

ivofivsev=[(10+key[j])%12, (1+key[j])%12, (5+key[j])%12, (8+key[j])%12, (9+key[j])%12]

viidimofVI=[(7+key[j])%12, (10+key[j])%12, (1+key[j])%12, -1, -1]

viidimofVIsev=[(7+key[j])%12, (10+key[j])%12, (1+key[j])%12, (4+key[j])%12, (5+key[j])%12]

viidimofVII=[(9+key[j])%12, (0+key[j])%12, (3+key[j])%12, -1, -1]

viidimofVIIsev=[(9+key[j])%12, (0+key[j])%12, (3+key[j])%12, (6+key[j])%12, (7+key[j])%12]




