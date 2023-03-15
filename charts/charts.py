import matplotlib.pyplot as pyplot



def generate_pie_chart():
    labels = ['A','B','C']
    values = [200,100,150]
    fig,ax = pyplot.subplots()
    ax.pie(values,labels=labels)
    pyplot.savefig('pie.png')
    pyplot.close()


if __name__ == "__main__":
    generate_pie_chart()















'''
import matplotlib.pyplot as pyplot

def generate_pie_chart():
    labels =['A','B','C']
    values = [200,34,120]

    fig,ax = pyplot.subplots()
    ax.pie(values,labels = labels)
    pyplot.savefig('.pie.png')
    pyplot.close()

'''





