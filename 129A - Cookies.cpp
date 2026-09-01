#include <bits/stdc++.h>
using namespace std;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    long long n,ce=0,co=0,val;
    cin>>n;
    for (int i=0;i<n;++i){
        cin>>val;
        if (val%2==0){
            ce+=1;
        }else{
            co+=1;
        }
    }
    if (co==0){
        cout<<n<<"\n";
    }if (co%2==0 && co!=0){
        cout<<ce<<"\n";
    }if (co%2!=0){
        cout<<co<<"\n";
    }
}
