; Generates a Newton fractal of sin(x), coloring the pixels by the 
; converged root and number of iterations required for convergence. The 
; code generally takes a long time to run, but should complete within 
; approximately an hour.

; The function newton returns a list, where car(list) is the converged 
; root and cdr(list) is the number of iterations.

(define max-iterations 50)

(define (newton z k)
	(let ((new-z (complex-sub z (tan z))))
		(if (or
				(>= k max-iterations)
				(< (complex-abs (complex-sub z new-z)) 1e-5))
			(list z k)
			(newton new-z (+ k 1)))))

; The function color-map maps the output from newton to a color, based on 
; root convergence and number of iterations.

(define e 2.718281828459045)
(define pi 3.141592653589793)
(define brightness -8)

(define (color-map input)
	(let
		((intensity (expt e (/ (car (cdr input)) brightness)))
		(n (if (null? (car input))
			nil
			(round (/ (car (complex-to-list (car input))) pi)))))
		(cond
			((null? n) (rgb 0 0 0))
			((even? n) (rgb 0 0 (* 0.5 intensity)))
			((odd? n) (rgb intensity (* 0.9 intensity) 0)))))

(pixelsize 1)

; The function coordinate-map maps a point (x, y) to a complex number 
; a + bi for use in Newton's method.

(define x-center (/ pi 2))
(define y-center 0)
(define x-window (/ pi 32))
(define y-window-unscaled (/ pi 32))
(define y-window (* y-window-unscaled (screen_height) (/ (screen_width))))
(define x-start (- x-center x-window))
(define y-start (- y-center y-window))
(define x-res (* 2 x-window (/ (screen_width))))
(define y-res (* 2 y-window (/ (screen_height))))

(define (coordinate-map x y)
	(complex (+ (* x x-res) x-start) (+ (* y y-res) y-start)))

; The draw function colors every pixel according to color-map. This 
; function may take up to an hour to run.

(define (draw)
	(define (draw-iter x y)
		(cond
			((> y (screen_height)) 'okay)
			((> x (screen_width)) (draw-iter 0 (+ y 1)))
			(else (begin
				(pixel x y
					(color-map (newton (coordinate-map x y) 0)))
				(draw-iter (+ x 1) y)))))
	(draw-iter 0 0))