class Solution {
public:
    int divide(int dvd, int dvi) {
        if (dvd == dvi)
            return 1;
        if (dvd == 0)
            return 0;
        bool flag = false;
        if (dvd < 0 || dvi <0)
           flag = true;
        
        if (dvd < 0 && dvi <0)
           flag = false;

        long long a = llabs(dvd);
        long long b = llabs(dvi);
        long long res = 0;

        while (a >= b ){
            int q =0;
          
            while (a >= b << (q+1))
                 q++;
            
            res += (1 << q);
            a -= (b<<q);
        }
        
        if (res == INT_MIN && !flag)
            return INT_MAX;

        return flag ? -res : res;
        
    }
};