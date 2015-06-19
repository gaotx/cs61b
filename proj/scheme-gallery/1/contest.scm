

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

(define (box func1 dist func2 angle k max)

	(define (repeat func1 dist func2 angle k counter)
		(cond 
			((> counter 0) (begin (random_repeat func1 dist k) (func2 angle) (repeat func1 dist func2 angle k (- counter 1))))
			(else (func1 .0001))))

	(cond ((= max 0) (bgcolor (rgb .3 .6 .8)))
		  (else (begin (repeat func1 dist func2 angle k 2) (box func1 dist func2 angle (+ k 1) (- max 1))))))
	
		
(define (random_repeat func arg k)
	(cond ((= 0 k) (func arg))
		  (else (begin (func arg) (random_repeat func arg (- k 1)))
		)))


(bgcolor (rgb .3 .6 .8))
(box fd 10 rt 90 2 56)