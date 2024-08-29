import turtle as t

n = 5
t.shape('turtle')
for i in range(5):
    t.fd(100)
    t.lt(360/5)
    t.fd(100)
    t.rt((360/5)*2)

t.mainloop()