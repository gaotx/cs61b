; Call expressions

(+ 1 2 3 4)

(+)

(*)

(- 12)

(- 20 1 2 3 4 5)

(/ (+ (* (- (* 2 2 2 2 2 3 3 3) 1) 7) 4) 3)

(number? 12)

(integer? 3.3)

(zero? 2)

; Definitions

(define (square x) (* x x))

(define (average x y) (/ (+ x y) 2))

(define (abs x)
  (if (< x 0)
      (- x)
      x))

(define (sqrt x)
  (define (improve guess)
    (average guess (/ x guess)))
  (define (sqrt-iter guess)
    (if (= (square guess) x)
        guess
        (sqrt-iter (improve guess))))
  (sqrt-iter 1))

; Pairs

(define (length items)
  (if (null? items)
      0
      (+ 1 (length (cdr items)))))

(define (getitem items n)
  (if (= n 0)
      (car items)
      (getitem (cdr items) (- n 1))))

(define squares (list 1 4 9 16 25))

(length squares)

(getitem squares 3)

; Sierpinski

(define (repeat k fn)
  ; Repeat fn k times.
  (if (> k 1)
      (begin (fn) (repeat (- k 1) fn))
      (fn)))

(define (tri fn)
  ; Repeat fn 3 times, each followed by a 120 degree turn.
  (repeat 3 (lambda () (fn) (lt 120))))

(define (sier d k)
  ; Draw three legs of Sierpinski's triangle to depth d.
  (tri (lambda ()
         (if (= k 1) (fd d) (leg d k)))))

(define (leg d k)
  ; Draw one leg of Sierpinski's triangle to depth d.
  (sier (/ d 2) (- k 1))
  (penup)
  (fd d)
  (pendown))

(sier 400 6)
