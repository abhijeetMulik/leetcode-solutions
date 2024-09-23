class Solution {
    public int[] intersection(int[] nums1, int[] nums2) {

        Set<Integer> set1 = new HashSet<>();
        for(int a : nums1){
            set1.add(a);
        }

        Set<Integer> set2 = new HashSet<>();
        for(int a : nums2){
            set2.add(a);
        }

        set1.retainAll(set2);

        int[] result = new int[set1.size()];

        int i = 0;
        for(int b: set1){
            result[i++] = b;
        }

        return result;





        
    }
}