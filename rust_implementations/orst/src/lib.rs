pub trait Sorter {
    fn sort<T>(slice: &mut [T]) 
    where 
        T: Ord;
}



pub fn sort<T, S>(slice: &mut [T]) where T: Ord, S:Sorter {
    S::sort(slice)
}

mod bubblesort;
mod insertion_sort;




#[cfg(test)]
mod tests {
    use std::vec;

    use super::*;

    struct StdSorter;
    
    impl Sorter for StdSorter {

        fn sort<T>(slice: &mut [T]) where T: Ord {
                slice.sort()
            }
    }

    #[test]
    fn std_works() {
        let mut things = vec![4,2,3,1];
        sort::<_,StdSorter>(&mut things);
        assert_eq!(things, &[1,2,3,4]);
    }
}
