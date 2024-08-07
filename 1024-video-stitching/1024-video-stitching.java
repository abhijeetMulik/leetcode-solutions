class Solution {
    public int videoStitching(int[][] clips, int time) {
        int start = 0;
        int end = 0;
        int count = 0;

        while(start < time) {
            for(int[] c : clips){
                if(start >= c[0]){
                    end = Math.max(end, c[1]);
                }
            }

            if(start == end){
                return -1;
            }
            count ++;
            start = end;
        }

        return count;
        
    }
}