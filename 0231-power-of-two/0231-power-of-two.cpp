class Solution {
public:
    bool isPowerOfTwo(int n) {

  if (n<0)
   {
    return false;
   }
  
  int m=n;
  int zero_count=0;
  int bit;

  while (m!=0)
  {
    bit= m & 1;
    
    if (bit==0)
    {
      zero_count++;
    }
    
    m = m >> 1; 

  }
  
  if(n==(pow(2,zero_count))){  
    return true;
  }
  else{ 
    return false;
  }
  
    }
};