import java.util.*;

public class FibonacciPartialSum_share {
    private static long getFibonacciPartialSumNaive(long from, long to) {
        int [] mem={0,1,1,2,3,5,8,3,1,4,5,9,4,3,7,0,7,7,4,1,5,6,1,7,8,5,3,8,1,9,0,9,9,8,7,5,2,7,9,6,5,1,6,7,3,0,3,3,6,9,5,4,9,3,2,5,7,2,9,1};
        long ans=0;
        long period=60;
        int start=(int)(from%period);
        int end=(int)(to%period);
        if(end<start){
            for(int iter=0;iter<=end;iter++)
            {
                ans=(ans+mem[iter])%10;
            }
            for(int iter=start;iter<period;iter++)
            {
                ans=(ans+mem[iter])%10;
            }
        }
        else
        {
            for(int iter=start;iter<=end;iter++)
            {
                ans=(ans+mem[iter])%10;
            }
        }
    return ans;
}    
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        long from = scanner.nextLong();
        long to = scanner.nextLong();
        System.out.println(getFibonacciPartialSumNaive(from, to));
    }
}

