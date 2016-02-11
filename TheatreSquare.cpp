/*
  Problem Link: http://codeforces.com/contest/1/problem/A
*/

#include <iostream>

using namespace std;

long long int ceil( long long int a, long long int b ) {
    return ( ( a + b - 1 ) / b );
}

long long int minSquares( long long int n, long long int m, long long int a ) {
    long long int x = ceil( n, a );
    long long int y = ceil( m, a );
    return ( x * y );
}

int main() {
    long long int n, m, a;
    cin >> n >> m >> a;
    cout << minSquares( n, m, a ) << endl;
    return 0;
}
