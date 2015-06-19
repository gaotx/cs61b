
(define (draw-spiral radius)
	(cond 
		((<= radius 75) (circle radius))
		(else (circle radius) (draw-spiral (- radius 2)))))

(define (draw-spiral-two radius)
	(cond 
		((<= radius 25) (circle radius))
		(else (circle radius) (draw-spiral (- radius 2)))))

(define (restart)
	(goto 0 0)
	(seth 0))

(define (fill-screen shade x y)
	(color shade)
	(penup)
	(goto (- 0 x) y)
	(pendown)
	(begin_fill)
	(goto x y)
	(goto x (- 0 y))
	(goto (- 0 x) (- 0 y))
	(goto (- 0 x) y)
	(end_fill))

(define (petal type)
	(cond
		((= type 1)
			(color "black")
			(draw-spiral 100)
			(left 90)
			(draw-spiral 100)
			(left 90)
			(draw-spiral 100)
			(left 90)
			(draw-spiral 100)
			(color "red")
			(draw-spiral 99)
			(left 90)
			(draw-spiral 99)
			(left 90)
			(draw-spiral 99)
			(left 90)
			(draw-spiral 99)
			(left 90))
		(else
			(color "black")
			(draw-spiral-two 50)
			(left 90)
			(draw-spiral-two 50)
			(left 90)
			(draw-spiral-two 50)
			(left 90)
			(draw-spiral-two 50)
			(color "yellow")
			(draw-spiral-two 49)
			(left 90)
			(draw-spiral-two 49)
			(left 90)
			(draw-spiral-two 49)
			(left 90)
			(draw-spiral-two 49)
			(left 90))))




(speed 10)
(fill-screen "white" 800 600)
(fill-screen "orange" 750 575)
(penup)
(restart)
(pendown)
(petal 1)
(penup)
(goto 200 200)
(pendown)
(left 45)
(petal 2)
(penup)
(goto 200 -200)
(pendown)
(petal 2)
(penup)
(goto -200 200)
(pendown)
(petal 2)
(penup)
(goto -200 -200)
(pendown)
(petal 2)







