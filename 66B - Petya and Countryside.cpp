#include <bits/stdc++.h>
using namespace std;

int main() 
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    vector<long long> a;
    long long n,val,ans=1;
    cin>>n;
    for (long long i=0;i<n;++i){
        cin>>val;
        a.push_back(val);
    }
    for (long long x=0;x<a.size();++x){
        long long prevlo=x,prevhi=x,lo=x-1,hi=x+1,cout=1;
        while (lo>=0){
            if (a[lo]<=a[prevlo]){
                cout+=1;
                prevlo-=1;
                lo-=1;
            }else{
                break;
            }
        }
        while (hi<a.size()){
            if (a[hi]<=a[prevhi]){
                cout+=1;
                prevhi+=1;
                hi+=1;
            }else{
                break;
            }
        }
        ans=max(ans,cout);
    }
    cout<<ans<<"\n";
}
