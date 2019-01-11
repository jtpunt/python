# Author: Jonathan Perry
# Date: 9/7/2018
def lcs(X, Y, i, j): 
    if i == 0 or j == 0: 
       return 0; 
    elif X[i-1] == Y[j-1]: 
       return 1 + lcs(X, Y, i-1, j-1); 
    else: 
       return max(lcs(X, Y, i, j-1), lcs(X, Y, i-1, j)); 
  
def main():
	X = "AGGTAB"
	Y = "GXTXAYB"
	print("Length of LCS is ", lcs(X , Y, len(X), len(Y)))

if __name__ == "__main__":
	main() 