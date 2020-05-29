//https://www.hackerearth.com/problem/algorithm/mancunian-and-k-ordered-lcs-e6a4b8c6/submissions/

#include<iostream>
#include<algorithm>
using namespace std;
long int lcs(long int n,long int m,vector <int> a,vector <int> b)
{
    vector<vector<int>> arr (n + 1, vector<int>(m + 1));
    long int i,j;
    for(i=0;i<n;i++)
    {
        for(j=0;j<m;j++)
        {
            if(a[i]==b[j])
            {
                arr[i+1][j+1]=arr[i][j]+1;
            }
            else
            {
                arr[i+1][j+1]=max(arr[i+1][j],arr[i][j+1]);
            }
        }
    }
    return arr[n][m];
}
int main()
{
    long int n,m,k;
    cin>>n>>m>>k;
	vector <int> a(n);
	vector <int> b(m);
    for(long int i=0;i<n;i++)
    {
        cin>>a[i];
    }
    for(long int i=0;i<m;i++)
    {
        cin>>b[i];
    }
    cout<<lcs(n,m,a,b)+k;
    return 0;
}
