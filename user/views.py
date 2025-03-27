from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.http import HttpResponse
# from rest_framework import status
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework import generics
from .models import User, Stocks, Transaction
# from googlefinance.client import get_price_data, get_prices_data, get_prices_time_data
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import xlrd
from django.conf import settings
import requests
import os
from sklearn.preprocessing import MinMaxScaler
import pickle


future = []


def scaling(X_train):
  X_train = X_train.reshape(-1, 1)
  sc = MinMaxScaler(feature_range=(0, 1))
  training_set_scaled = sc.fit_transform(X_train)
  return training_set_scaled, sc


def load_model(filename):
  reg = pickle.load(open(filename, 'rb'))
  return reg


def test_sol(X, sc, regressor):
  # X_t = X_test.reshape((-1, 1))
  # print(X_t.shape)
  var = X.reshape((-1, 1))
  # print(var.shape)
  # np.concatenate((X_train, X_test.reshape(-1, 1)), axis = 0)
  inputs = sc.transform(var)

  X_test = []
  # print(inputs.shape)
  for i in range(60, inputs.shape[0]):
    X_test.append(inputs[i-60:i, 0])

  X_test = np.array(X_test)
  # print("X_test.shape ", X_test.shape)
  # X_test.shape
  X_test = np.reshape(X_test, (X_test.shape[0], X_test.shape[1], 1))
  # print(X_test)
  # for i in range(0, 60):
  #  print(X_test[0][i], X_test[1][i])
  predicted_stock_price = regressor.predict(X_test)
  predicted_stock_price = sc.inverse_transform(predicted_stock_price)

  return predicted_stock_price  # X is real stock prices
# %matplotlib inline


def perpetual(count, X, sc, regressor):
  '''
  X should be shaped as 1, 60, 1
  '''
  for i in range(count):
    # print(X)
    # var = X_test = X.reshape((-1, 1)) #60, 1
    inputs = sc.transform(X)
    X_test = np.array(inputs)
    X_test = np.reshape(X_test, (X_test.shape[0], X_test.shape[1], 1))
    predicted_stock_price = regressor.predict(X_test)
    predicted_stock_price = sc.inverse_transform(predicted_stock_price)
    # print("predicted: ", predicted_stock_price)
    future.append(predicted_stock_price[0, 0])
    X = np.roll(X, -1)
    X[0, 59] = predicted_stock_price[0, 0]
    # print(X)


def plotit(real_stock_price, predicted_stock_price,i):
  # real_stock_price = X
  plt.plot(real_stock_price, color='red', label='Real Google Stock Price')
  a = np.average(real_stock_price)
  p = np.zeros((60, 1))
  p.fill(a)
  print(p)
  predicted_stock_price = np.concatenate((p, predicted_stock_price), axis=0)
  plt.plot(predicted_stock_price, color='blue',
           label='Predicted Google Stock Price')
  plt.title('Google Stock Price Prediction')
  plt.xlabel('Time')
  plt.ylabel('Google Stock Price')
  plt.legend()
  # plt.show() # SAVE IT
  final_path = settings.PROJECT_ROOT + '/user/static/img/'+i+'.png'
  plt.savefig(final_path)


def getStocks(request):

  symb = {'Microsoft': 'MSFT', 'Google': 'GOOG', 'Barclays': 'BCS',
          'JP Morgan Chase': 'JPM', 'Bank of america': 'bac'}
  for i in symb.values():
    #if file.storage.exists(self.file.name):
    #if (i+".npy")
    print('https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=' +
          i+'&apikey=62Q1OEQMZI876K16')
    response = requests.get(
        'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol='+i+'&apikey=62Q1OEQMZI876K16')
    stocks = response.json()
# filename = stocks
# suffix = '.json'
# with open(()) as f:
    data = stocks

    d = data['Time Series (Daily)']  # Time Series (Digital Currency Daily)

    dates = d.keys()

    _open = []
    _close = []
    _high = []
    _low = []
    _value = []

    for date in d:
      _close.append(float(d[date]['4. close']))  # 4a. close (USD)

    print(len(_close))

    k = np.array(_close).reshape(len(_close), 1)

    print(k)

    # from tempfile import TemporaryFile
    # outfile = TemporaryFile()
    filename = i
    np.save(filename, k)
    print('here')
    filename = os.path.dirname(os.path.realpath(__file__)) + '/'+i+'.npy'
    X = X_train = np.load(filename)

    training_set_scaled, sc = scaling(X_train)
    model = os.path.dirname(os.path.realpath(__file__)) + '/hundred_epochs.pkl'
    regressor = load_model(model)
    predicted_stock_price = test_sol(X_train, sc, regressor)
    real_stock_price = X_train

    # perpetual()

    A = real_stock_price.reshape(-1, 1)
    temp = A[-60:].reshape(1, 60)
    # print(temp)
    say = A[0:60, 0].reshape(60, 1)
    perpetual(5, temp, sc, regressor)
    F = np.array(future)
    F = F.reshape(F.shape[0], 1)
    B = predicted_stock_price.reshape(-1, 1)
    B = np.concatenate((B, F), axis=0)
    # B = np.concatenate((B, F), axis=0)
    # for i, j in zip(A, B):
    #  print(i, j)
    # from datetime import datetime
    # from datetime import timedelta
    # date = datetime.strptime(dates[-1], '%Y-%m-%d')
    print(date)
    plotit(A, B, i)
    # print()
    # return render(request, 'stockpage.html')

  return render(request, 'stockpage.html')


def plot_bar_x(prices, time, cityname):
    # this is for plotting purpose
  index = np.arange(len(time))
  plt.bar(index, prices)
  plt.xlabel('Year', fontsize=15)
  plt.ylabel('Price per square feet', fontsize=5)
  plt.xticks(index, time, fontsize=5)
  plt.title(cityname)
  # plt.figure(figsize=(40, 30))
  # plt.show()
  print(cityname)
  filename = settings.PROJECT_ROOT + '/user/static/img/'+cityname+'.png'
  plt.savefig(filename)
  return


def login(request):
  return render(request, 'login.html')


def enter(request):
  if User.objects.filter(username=request.POST.get('username'), password=request.POST.get('password')).exists():
    u = User.objects.get(username=request.POST['username'])
    request.session['usid'] = u.id
    context = {'user': u}
    return render(request, 'landingpage.html', context)
  else:
    e = "User doesn't exist"
  return render(request, 'landingpage.html', {'error': e})


def home(request):
  usr = User.objects.filter(id=request.session['usid'])
  for i in usr:
    u = i
  return render(request, 'landingpage.html', {'u': u})


def stock(request):
  stock_list = Stocks.objects.all()
  return render(request, 'stockpage.html', {'Stocks': stock_list})


def signup(request):
  return render(request, 'signup.html')


def register(request):
  u = User()
  u.email = request.POST.get('email')
  u.name = request.POST.get('name')
  u.password = request.POST.get('password')
  u.mobile = request.POST.get('mobile')
  u.username = request.POST.get('username')
  error = ""
  if(u.password == request.POST.get('reppassword')):
    u.save()
    return render(request, 'login.html')
  else:
    error = "Password didn't match"

  return render(request, 'signup.html', {"error": error})


def mystock(request):
  s = Stocks.objects.all()
  t = Transaction.objects.filter(user=request.session['usid'])
  us = []
  st = []

  for j in t:
    us.append(j.stock)

  # print("jdygf",us)
  for i in s:
    if i.name in us:
      st.append(i)
  print("user", st)
  return render(request, 'profile.html', {'st': us})


def profile(request):
  usr = User.objects.filter(id=request.session['usid'])
  for i in usr:
    u = i
  return render(request, 'home.html', {'u': u})


def deleteStocks(request, slug):
  s = Stocks.objects.filter(id=slug)
  usr = User.objects.filter(id=request.session['usid'])
  for j in s:
    for i in usr:
      u = Transaction.objects.filter(user=i, stock=j)
      for j in u:
        loss = j.Val
        j.delete()

  usr = User.objects.filter(id=request.session['usid'])
  for i in usr:
    no = i.stock_no
    val = i.portfolio_val

  # Transaction.objects.filter(user=request.session['usid'],stock = slug).delete()
  usr.update(stock_no=no - 1, portfolio_val=val - loss)
  return render(request, 'stockpage.html')


def addStocks(request, slug):
  s = Stocks.objects.filter(id=slug)
  s.update(quantity=int(request.POST.get('qts')))
  u = User.objects.filter(id=request.session['usid'])

  for i in u:
    uuu = i

  for i in s:
    sss = i
    cls = i.close
    # new.stock = slug

  # new.save()
  if request.method == 'POST':

    v = cls * int(request.POST.get('qts'))
    u = User.objects.filter(id=request.session['usid'])
    for i in u:
      p = i.stock_no
      port = i.portfolio_val
      # p = i.stock
    # slug = p.append(slug)
    t = Transaction(stock=sss, user=uuu, quantity=int(
        request.POST.get('qts')), Val=v)
    t.save()
    u = User.objects.filter(id=request.session['usid']).update(
        stock_no=p+1, portfolio_val=port+v)

  return render(request, 'profile.html')


def house(request):
  return render(request, 'house.html')


def getBar(request):
  city = request.POST.get('dropdown')
  q = settings.PROJECT_ROOT+'/user/HPI@Assessment Prices_Prices.xls'
  xls = pd.ExcelFile(q)
  sheetX = xls.parse(0)  # 0 is the sheet number
  # uniquecitynames= sheetX['City'].unique()
  df = sheetX
  print(sheetX.groupby(['City']).groups.keys())
  prices = df.loc[df['City'] == city]
  # print(prices['Composite Price'])
  pricevalues = prices['Composite Price']
  time = prices['Quarter']
  plot_bar_x(pricevalues, time, city)
  return render(request, 'house.html')


def logout(request):
  return render(request, 'login.html')


def about(request):
  return render(request, 'about.html')


def know(request):
  return render(request, 'Jargons.html')
