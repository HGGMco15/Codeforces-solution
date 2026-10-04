#include <bits/stdc++.h>
using namespace std;

int main() 
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    long long a,b;
    cin>>a>>b;
    long long c=max(a,b);
    long long div=gcd((6-c+1),6);
    cout<<(long long)((6-c+1)/div)<<"/"<<(long long)(6/div)<<"\n";
}
