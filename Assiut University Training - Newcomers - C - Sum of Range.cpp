#include <bits/stdc++.h>
using namespace std;
void solve(){
    long long a,b;
    cin>>a>>b;
    if (a>=b){
        swap(a,b);
    }
    cout<<((a+b)*(b-a+1)/2)<<"\n";
    if(a%2==0){
        if(b%2==0){
            cout<<(long long)((a+b)*((b-a)/2+1)/2)<<"\n";
            cout<<(long long)(((a+1)+(b-1))*(((b-1)-(a+1))/2+1)/2)<<"\n";
        }else{
            cout<<(long long)((a+(b-1))*(((b-1)-a)/2+1)/2)<<"\n";
            cout<<(long long)(((a+1)+b)*((b-(a+1))/2+1)/2)<<"\n";
        }
    }else{
        if(b%2==0){
            cout<<(long long)(((a+1)+b)*((b-(a+1))/2+1)/2)<<"\n";
            cout<<(long long)((a+(b-1))*(((b-1)-a)/2+1)/2)<<"\n";
        }else{
            cout<<(long long)(((a+1)+(b-1))*(((b-1)-(a+1))/2+1)/2)<<"\n";
            cout<<(long long)((a+b)*((b-a)/2+1)/2)<<"\n";
        }
    }
}
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    solve();
    return 0;
}
