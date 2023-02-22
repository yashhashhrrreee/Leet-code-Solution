public class Solution {
        public int shipWithinDays(int[] weights, int days) {
    
    int sum = 0;
    
    int max = Integer.MIN_VALUE;
    
    for( int i = 0; i < weights.length; i++ ) {
        sum+=weights[i];
        max = Math.max(max, weights[i]);
    }
    
    int l = max, r = sum;
    
    while( l < r ){
        
        int mid = l + (r-l)/2;
        
        if( canShipWithCapacity(mid, weights, days ) ){
            r = mid;
        }else{
            l = mid+1;
        }
        
    }
    
    return l;
}

private boolean canShipWithCapacity(int capacity,int[] weights, int days){
    
    int currWeight = 0, currDays = 1;
    for( int w : weights ){
        currWeight += w;
        if( currWeight > capacity ){
            currWeight = w;
            currDays++;
            if( currDays > days ) return false;
        }
    }
    
    return true;
}
}