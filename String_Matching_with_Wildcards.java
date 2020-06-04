//https://www.hackerrank.com/contests/placement-preparation-1/challenges/string-matching-with-wildcards/problem

import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s1 = sc.nextLine().trim();
        String s2 = sc.nextLine().trim();
        boolean dp[][] = new boolean[s1.length()+1][s2.length()+1];
        dp[0][0]=true;
        for(int i=1;i<=s1.length();i++){
            if(s1.charAt(i-1)=='*'){
                dp[i][0]= true;
            }else{
                break;
            }
        }
        for(int i=1;i<=s1.length();i++){
            for(int j= 1;j<=s2.length();j++){
                if(s1.charAt(i-1)==s2.charAt(j-1) || s1.charAt(i-1)=='?'){
                    dp[i][j]= dp[i-1][j-1];
                }else if(s1.charAt(i-1)=='*'){
                    dp[i][j]= dp[i-1][j] || dp[i][j-1];
                }else{
                    dp[i][j]= false;  
                }
            }
        }
        if(dp[s1.length()][s2.length()]==true){
            System.out.println("TRUE");
        }else{
            System.out.println("FALSE"); 
        }
    }
}
