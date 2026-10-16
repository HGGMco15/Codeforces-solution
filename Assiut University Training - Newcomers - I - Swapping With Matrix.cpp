#include <bits/stdc++.h>
using namespace std;
#define int long long
void swapcol(vector<vector<long long>> &matrix,long long col1,long long col2){
    col1-=1;col2-=1; //based 1 index
    for (size_t i=0;i<matrix.size();++i){
        swap(matrix[i][col1],matrix[i][col2]);
    }
}
void swaprow(vector<vector<long long>> &matrix,long long row1,long long row2){
    row1-=1; row2-=1;
    swap(matrix[row1],matrix[row2]);
}
signed main() 
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    vector<vector<long long>> a;
    long long n,x,y,val;
    cin>>n>>x>>y;
    for (long long j=0;j<n;++j){
        vector<long long> b;
        for (long long h=0;h<n;++h){
            cin>>val;
            b.push_back(val);
        }
        a.push_back(b);
    }
    swaprow(a,x,y);
    swapcol(a,x,y);
    for (const auto& rw:a){
        for (int i:rw){
            cout<<i<<" ";
        }
        cout<<"\n";
    }
    return 0;
}
