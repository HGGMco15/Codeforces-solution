#include <bits/stdc++.h>
using namespace std;
bool palindrome(const string& s){
    return equal(s.begin(),s.begin()+s.size()/2,s.rbegin());
}
bool isReversed(const string& s1, const string& s2) {
    if (s1.size() != s2.size()) return false;
    return equal(s1.begin(), s1.end(), s2.rbegin());
}
int main() 
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    string val;
    vector<string> a;
    for (long long i=0;i<3;++i){
        cin>>val;
        a.push_back(val);
    }
    bool res=isReversed(a[0],a[2]);
    if (res){
        if (palindrome(a[1])){
            cout<<"YES"<<"\n";
        }else{
            cout<<"NO"<<"\n";
        }
    }else{
        cout<<"NO"<<"\n";
    }
}
