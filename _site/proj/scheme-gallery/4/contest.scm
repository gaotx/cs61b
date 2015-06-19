
(define (sun length angle sides count color_used)
  (color color_used)
  (cond ((= count 120) (pu))
      ((= sides 5) (sun (* length (/ 97 100)) (+ angle 10) 0 (+ count 1) color_used))
      ((= sides 1) (sun length (- angle 10) 2 count color_used))
      ((= count 3) (define color_used "#FA8F7C") (sun length angle (+ sides 1) count color_used))
      ((= count 5) (define color_used "#F9826D") (sun length angle (+ sides 1) count color_used))
      ((= count 8) (define color_used "#FA735B") (sun length angle (+ sides 1) count color_used))
      ((= count 15) (define color_used "#F86248") (sun length angle (+ sides 1) count color_used))
      ((= count 30) (define color_used "#F75133") (sun length angle (+ sides 1) count color_used))
      ((= count 60) (define color_used "#F73F1E") (sun length angle (+ sides 1) count color_used))
      ((= count 80) (define color_used "#F73310") (sun length angle (+ sides 1) count color_used))
      (else
          (fd length)
          (left angle)
          (sun length angle (+ sides 1) count color_used))
  )

)
(pu)
(goto -250 200)
(pd)
(sun 400 280 0 0 "#F99D8C")

;;; THE HAIKU

; (Sally could have sold 
; 	More seashells if she had not
; 		Sold by the seashore)









