#include <bits/stdc++.h>
using namespace std;
 
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    long long t,a,b,c,d;
    cin>>t;
    for (long long i=0;i<t;++i){
        cin>>a>>b>>c>>d;
        if (a==b && b==c && c==d){
            cout<<"YES"<<"\n";
        }else{
            cout<<"NO"<<"\n";
        }
    }
    return 0;
}
