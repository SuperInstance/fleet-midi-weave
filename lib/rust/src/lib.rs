pub fn process(v: &[i8], base: u8) -> Vec<u8> {
    let mut notes = vec![base];
    for &x in v {
        let last = notes.last().copied().unwrap_or(base);
        notes.push(if x == 1 { last + 4 } else if x == -1 { last.wrapping_sub(4) } else { last });
    }
    notes
}
#[cfg(test)]
mod tests {
    use super::*;
    #[test] fn test_process() {
        let v = [1,0,-1,1,0,-1,1,1];
        let r = process(&v, 60);
        assert_eq!(r, vec![60,64,64,60,64,64,60,64,68]);
    }
}
