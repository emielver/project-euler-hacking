import java.math.BigInteger;

public class Problem121{
  public static void main(String[] args){
    
    // Winning combinations include 4 blues in the end and 3 blues + 1 red in the end.
    // The chance of 4 blues is 1/2 * 1/3 * 1/4 * 1/5 = 1/120
    // The chance of 3 blues and 1 red is:
    // 1/2 * 1/3 * 1/4 * 1/5 +
    // 1/2 * 2/3 * 1/4 * 1/5 +
    // 1/2 * 1/3 * 3/4 * 1/5 +
    // 1/2 * 1/3 * 1/4 * 4/5 =
    // 1/120 + 2/120 + 3/120 + 4/120
    
    // Second attempt: making a tree seems a better idea
    
    int n = 15;
    
    // Initialize the 0th and (after) the 1st step
    BigInteger [][] a = new BigInteger[n+1][n+1];       // I set row and column 0 to '0';
    a[0][0] = BigInteger.valueOf(0);
    a[1][0] = BigInteger.valueOf(1);                   // We forget about the denominator, as it will be n! in every step
    a[1][1] = BigInteger.valueOf(1);
    
    // The probability of only blues is in the most left column, the numerator will always be 1.
    for (int i = 2; i <= n; i++){
      a[i][0] = BigInteger.valueOf(1);                        
      for (int j = i; j < i+1; j++){
        a[i][j] = factorial(i);       // The numerator of the probability of only red is 1! after step 1, 2! after step 2, 3! after step 3 etc
      }
    }
    
    
    // For all the values not on the boundary, the value is the sum of going from previous state (above left in matrix) + 1 red. Added by the above right + 1 blue
    for (int x = 2; x <= n; x++){
      for (int z = 1; z <= x-1; z++){
        a[x][z] = a[x-1][z-1].multiply(BigInteger.valueOf(x));
        a[x][z] = a[x][z].add(a[x-1][z]);
      }
    }
    
    for (int k = 0; k <= n; k++){
      for (int m = 0; m < n; m++){
        System.out.print(a[k][m] + " ");
      }
      System.out.println();
    }
    
    BigInteger sum = new BigInteger("0");
    for (int j = 0; j <= 7; j++){
      sum = sum.add(a[n][j]);
    }
    System.out.println("The numerator of the probability of blue > red: " + sum);
    BigInteger denom = factorial(n+1);
    BigInteger outcome = denom.divide(sum);
    System.out.println("The maximum price for this game should be: " + outcome);
  }
  
  
  
  
  
  // Method to return factorial biginteger
  public static BigInteger factorial (int n){
    
    if (n == 1){
      return BigInteger.valueOf(1);
    }
    else{
      BigInteger nn = BigInteger.valueOf(n);
      return nn.multiply(factorial(n-1));
    }
  }
}
    
    
    
    
      
    