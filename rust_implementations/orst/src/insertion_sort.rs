use super::Sorter;

pub struct Insertionsort;


impl Sorter for Insertionsort {
    
    
    fn sort<T>(slice: &mut [T]) where T: Ord {
        
        // [sorted | not sorted]
        // sorted starts out empty
        

        
        
        }

        
    }

}


#[test]
    fn bubble_sort_works() {
        let mut things = vec![4,2,5, 3,1];
        super::sort::<_,Insertionsort>(&mut things);
        assert_eq!(things, &[1,2,3,4,5]);
    }