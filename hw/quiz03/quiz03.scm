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
  ; YOUR-CODE-HERE
  'replace-this)

(define (how-many-dots s)
  ; YOUR-CODE-HERE
  'replace-this)
