
(define (deep-map fn s)
  (cond ((null? s) s)
        ((list? (car s)) (cons (deep-map fn (car s))
                               (deep-map fn (cdr s))))
        (else (cons (fn (car s))
                    (deep-map fn (cdr s)))))
)

(define (substitute s old new)
  (deep-map (lambda (x) (if (eq? old x) new x)) s)
)

(define (sub-all s olds news)
  (if (null? olds)
    s
    (sub-all (substitute s (car olds) (car news))
                     (cdr olds)
                     (cdr news)))
)


