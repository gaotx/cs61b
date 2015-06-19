; Load this file into an interactive session with:
; python3 scheme -load quiz03.scm

(define (map f s)
  ; List the result of applying f to each element in s.
  (if (null? s) s
    (cons (f (car s)) (map f (cdr s)))))

(define (filter f s)
  ; List the elements of s for which f returns a true value.
  (if (null? s) s
    (let ((rest (filter f (cdr s))))
      (if (f (car s)) (cons (car s) rest) rest))))

(define (no-repeats s)
  (if (null? s) s
    (cons (car s)
      (no-repeats (filter (lambda (x) (not (= (car s) x))) (cdr s))))))

(define (how-many-dots s)
  (if (not (pair? s)) 0
    (+ (if (and (not (pair? (cdr s))) (not (null? (cdr s)))) 1 0)
       (how-many-dots (car s))
       (how-many-dots (cdr s))))
