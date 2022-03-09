from flask import Blueprint, render_template, request, jsonify, redirect, url_for, current_app
import numpy as np

views = Blueprint('views', __name__)




lone_mat = 'calculator/lone_mat.html'

return_template = 'calculator/return.html'



@views.route('/Add', methods=['POST', 'GET'])
def add():
    row_num = 3
    col_num = 3
    if request.method == 'POST' and request.form.get('row_num') :
        row_num = int(request.form['row_num'])
        col_num = int(request.form['col_num'])
        return render_template('calculator/addition.html', row_num=row_num, col_num=col_num)
    elif request.method == 'POST' and request.form.get('mat1[]'):
        mat1_inp = request.form.getlist('mat1[]')
        mat2_inp = request.form.getlist('mat2[]')
        inp_iterator = 0
        row_num = int(request.form['row_n'])
        col_num = int(request.form['col_n'])
        result = np.zeros((row_num, col_num))
        mat1 = np.zeros((row_num, col_num))
        mat2 = np.zeros((row_num, col_num))
        for i in range(row_num):
            for j in range(col_num):
                try:
                    mat1[i][j] = float(mat1_inp[inp_iterator])
                    mat2[i][j] = float(mat2_inp[inp_iterator])
                    inp_iterator += 1
                except:
                    return "Error parsing Data"
        
        result = mat1 + mat2
        
        return render_template(return_template, op='add', mat1=mat1, mat2=mat2, result=result)


    else:
        return render_template('calculator/addition.html', row_num=row_num, col_num=col_num)
    
@views.route('/sub', methods=['POST', 'GET'])
def sub():
    row_num = 3
    col_num = 3
    if request.method == 'POST' and request.form.get('row_num') :
        row_num = int(request.form['row_num'])
        col_num = int(request.form['col_num'])
        return render_template('calculator/subtraction.html', row_num=row_num, col_num=col_num)
    elif request.method == 'POST' and request.form.get('mat1[]'):
        mat1_inp = request.form.getlist('mat1[]')
        mat2_inp = request.form.getlist('mat2[]')
        inp_iterator = 0
        row_num = int(request.form['row_n'])
        col_num = int(request.form['col_n'])
        result = np.zeros((row_num, col_num))
        mat1 = np.zeros((row_num, col_num))
        mat2 = np.zeros((row_num, col_num))
        for i in range(row_num):
            for j in range(col_num):
                try:
                    mat1[i][j] = float(mat1_inp[inp_iterator])
                    mat2[i][j] = float(mat2_inp[inp_iterator]) 
                    inp_iterator += 1
                except:
                    return "Error parsing Data"
        result = mat1-mat2
        
        return render_template(return_template, op='sub', mat1=mat1, mat2=mat2, result=result )


    else:
        return render_template('calculator/subtraction.html', row_num=row_num, col_num=col_num)

@views.route('/mul', methods=['POST', 'GET'])
def mul():
    row_num1 = 3
    col_num1 = 3
    col_num2 = 3
    row_num2 = 3
    if request.method == 'POST' and request.form.get('row_num1'):
        try:
            row_num1 = int(request.form['row_num1'])
            col_num1 = int(request.form['col_num1'])
            row_num2 = int(request.form['row_num2'])  
            col_num2 = int(request.form['col_num2'])
            if col_num1 != row_num2:
                return "Dimensions incompatiable for multiplication"  
            return render_template('calculator/mul.html',row_num1=row_num1, col_num1=col_num1, row_num2=row_num2, col_num2=col_num2 )
        except:
            return "please fill up the dimensions properly!!!"
    elif request.method == 'POST' and request.form.get('mat1[]'):
        mat1_inp = request.form.getlist('mat1[]')
        mat2_inp = request.form.getlist('mat2[]')
        row_num1 = int(request.form['row_n1'])
        col_num1 = int(request.form['col_n'])
        row_num2 = int(request.form['col_n'])
        col_num2 = int(request.form['col_n2'])
        mat1 = np.zeros((row_num1, col_num1))
        mat2 = np.zeros((row_num2, col_num2))
        inp_iterator = 0
        for i in range(row_num1):
            for j  in range(col_num1):
                try:
                    mat1[i,j] = float(mat1_inp[inp_iterator])
                    inp_iterator += 1
                except:
                    return "failed to parse input"
        inp_iterator = 0
        for i in range(row_num2):
            for j in range(col_num2):
                try:
                    mat2[i,j] = float(mat2_inp[inp_iterator])
                    inp_iterator += 1
                except:
                    return "Fatal error!! unable to parse input"
        result = np.matmul(mat1, mat2)
        return render_template(return_template, op='mul', mat1=mat1, mat2=mat2, result=result)
    else:
        return render_template('calculator/mul.html',row_num1=row_num1, col_num1=col_num1, row_num2=row_num2, col_num2=col_num2 )


@views.route('/trace_mat', methods=['POST', 'GET'])
def trace_mat():
    row_num = 3
    col_num = 3
    if request.method == 'POST' and request.form.get('row_num'):
        row_num = int(request.form['row_num'])
        col_num = int(request.form['col_num'])
        return render_template('calculator/trace.html', row_num=row_num, col_num=col_num)
    
    elif request.method == 'POST' and request.form['mat[]']:
        print(request.form)
        mat_inp = request.form.getlist('mat[]')
        inp_iterator = 0
        row_num = int(request.form['row_n'])
        col_num = int(request.form['col_n'])
        mat = np.zeros((row_num, col_num))
        print(row_num, col_num)
        for i in range(row_num):
            for j in range(col_num):
                try:
                    mat[i][j] = float(mat_inp[inp_iterator])
                    inp_iterator += 1
                except:
                    return "Wrong Input or problem with backend"
        trace = np.trace(mat)
        
        return render_template(return_template, op= 'trace',mat=mat, trace=trace)
    else:
        return render_template('calculator/trace.html', row_num=row_num, col_num=col_num)
                
@views.route('/determnt', methods=['POST', 'GET'])
def det():
    row_num = 3
    col_num = 3
    if request.method == 'POST' and request.form.get('row_num'):
        row_num = int(request.form['row_num'])
        col_num = int(request.form['col_num'])
        if row_num == col_num :
            return render_template('calculator/determinant.html', row_num=row_num, col_num=col_num)
        else:
            return "Row number and Column number should be same. "

    elif request.method == 'POST' and request.form['mat[]']:
        print(request.form)
        mat_inp = request.form.getlist('mat[]')
        inp_iterator = 0
        row_num = int(request.form['row_n'])
        col_num = int(request.form['col_n'])
        mat = np.zeros((row_num, col_num))
        print(row_num, col_num)
        for i in range(row_num):
            for j in range(col_num):
                try:
                    mat[i][j] = float(mat_inp[inp_iterator])
                    inp_iterator += 1
                except:
                    return "Wrong Input or problem with backend"
        det = np.linalg.det(mat)
        print(mat)
        
        return render_template('calculator/return.html', op='determnt', mat=mat, det=det)     
    else:
        return render_template('calculator/determinant.html', row_num=row_num, col_num=col_num)


@views.route('/inverse_mat', methods=['POST', 'GET'])
def inverse_mat():
    row_num = 3
    col_num = 3
    if request.method == 'POST' and request.form.get('row_num'):
        row_num = int(request.form['row_num'])
        col_num = int(request.form['col_num'])
        if row_num == col_num :
            return render_template('calculator/inverse.html', row_num=row_num, col_num=col_num)
        else:
            return "Row number and Column number should be same. "

    elif request.method == 'POST' and request.form['mat[]']:
        print(request.form)
        mat_inp = request.form.getlist('mat[]')
        inp_iterator = 0
        row_num = int(request.form['row_n'])
        col_num = int(request.form['col_n'])
        mat = np.zeros((row_num, col_num))
        print(row_num, col_num)
        for i in range(row_num):
            for j in range(col_num):
                try:
                    mat[i][j] = float(mat_inp[inp_iterator])
                    inp_iterator += 1
                except:
                    return "Wrong Input or problem with backend"
        inverse = np.linalg.inv(mat)
        print(mat)
        
        return render_template(return_template, op='inversion', mat=mat, inverse=inverse)     
    else:
        return render_template('calculator/inverse.html', row_num=row_num, col_num=col_num)    


@views.route('/eigen_vals', methods=['POST', 'GET'])
def eigen_vals():
    row_num = 3
    col_num = 3
    if request.method == 'POST' and request.form.get('row_num'):
        row_num = int(request.form['row_num'])
        col_num = int(request.form['col_num'])
        if row_num == col_num :
            return render_template('calculator/eigen.html', row_num=row_num, col_num=col_num)
        else:
            return "Row number and Column number should be same. "

    elif request.method == 'POST' and request.form['mat[]']:
        print(request.form)
        mat_inp = request.form.getlist('mat[]')
        inp_iterator = 0
        row_num = int(request.form['row_n'])
        col_num = int(request.form['col_n'])
        mat = np.zeros((row_num, col_num))
        print(row_num, col_num)
        for i in range(row_num):
            for j in range(col_num):
                try:
                    mat[i][j] = float(mat_inp[inp_iterator])
                    inp_iterator += 1
                except:
                    return "Wrong Input or problem with backend"
        eigenvals = np.linalg.eigvals(mat)
        print(mat)
        
        return render_template(return_template, op='eigen_vals', mat=mat, eigenvals=eigenvals)     
    else:
        return render_template('calculator/eigen.html', row_num=row_num, col_num=col_num)    

    

@views.route('/rank_mat', methods=['POST', 'GET'])
def rank_mat():
    row_num = 3
    col_num = 3
    if request.method == 'POST' and request.form.get('row_num'):
        row_num = int(request.form['row_num'])
        col_num = int(request.form['col_num'])
        if row_num == col_num :
            return render_template('calculator/rank.html', row_num=row_num, col_num=col_num)
        else:
            return "Row number and Column number should be same. "

    elif request.method == 'POST' and request.form['mat[]']:
        print(request.form)
        mat_inp = request.form.getlist('mat[]')
        inp_iterator = 0
        row_num = int(request.form['row_n'])
        col_num = int(request.form['col_n'])
        mat = np.zeros((row_num, col_num))
        print(row_num, col_num)
        for i in range(row_num):
            for j in range(col_num):
                try:
                    mat[i][j] = float(mat_inp[inp_iterator])
                    inp_iterator += 1
                except:
                    return "Wrong Input or problem with backend"
        rank = np.linalg.matrix_rank(mat)
        print(mat)
        
        return render_template(return_template, op='rank_mat', rank=rank, mat=mat)     
    else:
        return render_template('calculator/rank.html', row_num=row_num, col_num=col_num)    






@views.route('/power_mat', methods=['POST', 'GET'])
def power_mat():
    row_num = 3
    col_num = 3
    if request.method == 'POST' and request.form.get('row_num'):
        row_num = int(request.form['row_num'])
        col_num = int(request.form['col_num'])
        if row_num == col_num:
            return render_template('calculator/power_mat.html', row_num=row_num, col_num=col_num)
        else:
            return "Number of rows and number of columns nust be same!!!"

    elif request.method == 'POST' and request.form['mat[]']:
        if request.form.get('power'):
            power = int(request.form['power'])
            mat_inp = request.form.getlist('mat[]')
            inp_iterator = 0
            row_num = int(request.form['row_n'])
            col_num = int(request.form['col_n'])
            mat = np.zeros((row_num, col_num))
            for i in range(row_num):
                for j in range(col_num):
                    try:
                        mat[i][j] = float(mat_inp[inp_iterator])
                    except:
                        return "Error parsing input!!!"
            power_mat = np.linalg.matrix_power(mat, power)
            return render_template(return_template, op='power_mat', power_mat=power_mat, power=power, mat=mat )        

    else:
        return render_template('calculator/power_mat.html', row_num=row_num, col_num=col_num)








@views.route('/linear_equations', methods=['POST', 'GET'])
def linear_equations():
    var_num = 3
    num_equations = 3
    if request.method == 'POST' and request.form.get('var_num'):
        var_num = request.form['var_num']
        num_equations = request.form['num_equations']
        return render_template('calculator/linear_equations.html', var_num = var_num, num_equations=num_equations)
    elif request.method == 'POST' and request.form.get('a[]'):
        a_inp = request.form.getlist('a[]')
        b_inp = request.form.getlist('b[]')
        var_num = int(request.form['var_n'])
        num_equations = int(request.form['num_eq'])
        a = np.zeros((num_equations, var_num))
        b = np.zeros((num_equations))
        inp_a_iterator = 0
        for i in range(num_equations):
            for j in range(var_num):
                try:
                    a[i, j] = float(a_inp[inp_a_iterator])
                    inp_a_iterator += 1
                except:
                    return "Error parsing data"
            try:
                b[i] = float(b_inp[i])
            except:
                return "error parsing data"
        
        solution = np.linalg.solve(a,b)

        return render_template(return_template, op='linear_eq',a=a, b=b, solution=solution )

    else:
        return render_template('calculator/linear_equations.html', var_num = var_num, num_equations=num_equations)

    