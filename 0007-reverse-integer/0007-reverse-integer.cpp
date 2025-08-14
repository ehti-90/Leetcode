class Solution {
public:
    int reverse(int x) {
    double rev=0;
    int hold;
    

    while (x!=0)
    {

      hold=x%10;
      x=x/10;
      rev=((rev*10)+hold);

       if (rev>=INT_MAX || rev<=INT_MIN)
      {
        return 0;
      }

    }

    return (int)rev;
  
    }
};