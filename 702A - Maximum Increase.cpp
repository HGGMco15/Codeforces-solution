#include <bits/stdc++.h>
using namespace std;

int main() 
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    vector<long long> a;
    long long n,val,mx=1,cur=1;
    cin>>n;
    for (long long i=0;i<n;++i){
        cin>>val;
        a.push_back(val);
    }
    for (long long x=1;x<a.size();++x){
        if (a[x]>a[x-1]){
            cur+=1;
        }else{
            mx=max(cur,mx);
            cur=1;
        }
    }
    mx=max(cur,mx);
    cur=1;
    cout<<mx<<"\n";
}
