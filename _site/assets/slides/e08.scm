; Code as data

(define (fact n) 
  (if (= n 0) 1 (* n (fact (- n 1)))))

(define (fact-exp n)
  (if (= n 0) 1 (list '* n (fact-exp (- n 1)))))

(define (fib n)
  (if (<= n 1) n (+ (fib (- n 2)) (fib (- n 1)))))

(define (fib-exp n)
  (if (<= n 1) n (list '+ (fib-exp (- n 2)) (fib-exp (- n 1)))))

; Homoiconicity (requires biwa-scheme, etc.)

(read (open-input-string "(+ 1     2)"))
(read (open-input-string "(define (fact n) (if (= n 0) 1 (* n (fact (- n 1)))))"))

; Quotation

'(1 2 3)
(quote (1 2 3))
(read (open-input-string "'(+ 1 2)"))

; Macro

(define-macro twice (lambda (expr) (list 'begin expr expr)))
(define (check val) (if val 'Passed 'Failed))
(define-macro (check expr) (list 'if expr ''Passed (list 'quote (list 'Failed:  expr))))

; For

(define (map fn vals) 
  (if (null? vals) 
      () 
      (cons (fn (car vals)) 
            (map fn (cdr vals)))))

(map (lambda (x) (* x x)) '(2 3 4 5))

(define-macro (for sym expr vals)
  (list 'map (list 'lambda (list sym) expr) vals))

; Quasi-quoting

(define-macro (check expr) `(if ,expr 'Passed '(Failed: ,expr)))

; Variable arguments

(define (count . args) (if (null? args) 0 (+ 1 (apply count (cdr args)))))
(define (nest first . rest) 
  (if (null? rest) 
      (list first) 
      (list first (apply nest rest))))

; Let

(define (caar s) (car (car s)))
(define (cadar s) (car (cdr (car s))))
(define (cars s) (if (null? s) () (cons (caar s) (cars (cdr s)))))
(define (cadrs s) (if (null? s) () (cons (cadar s) (cadrs (cdr s)))))

(define-macro (leet bindings expr)
  `((lambda ,(cars bindings) ,expr) ,@ (cadrs bindings)))

(leet ((a (+ 1 1)) (b (+ 2 2))) (+ a b))

; Capture

(define (say x) (print 'hi) x)
(define-macro (or-1 x y) `(if ,x ,x ,y))
(define-macro (or-2 x y) `(let ((z ,x)) (if z z ,y)))
(define z 3)
(or-2 false z)
