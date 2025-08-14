class Solution {
public:
    int subtractProductAndSum(int n) {
        
        
 int product=1;
 int sum=0;
  int a;
  int result;

  for(int i=1;true; i++){
      a=n%10;
      n=n/10;

      sum=a+sum;
      product=a*product;
      
      if (n==0)
      {
        break;
      }
      
    }
     
    
  result=product-sum;
  return result;
    }
};