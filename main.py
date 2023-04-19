import soundfile as sf
import matplotlib.pyplot as plt
from Signal_snd_effect import Signal


# Hiển thị dạng sóng thời gian
def signalPlot(signal1, signal2, name):
  plt.subplot(2, 1, 1)
  plt.plot(signal1.data)
  plt.title("Trước và sau khi thêm hiệu ứng " + name)
  plt.subplot(2, 1, 2)
  plt.plot(signal2.data)
  plt.show()

def showMenu():
  print("--------------------------------------")
  print("Chon hieu ung can tao:")
  print("1. Hieu ung echo")
  print("2. Hieu ung fade in, fade out")
  print("3. Hieu ung modulation")
  print("4. Hieu ung reverb")
  print("5. Hieu ung reversal")
  print("6. Thoat")
  print("--------------------------------------")

# Đọc file âm thanh
filename = 'input.wav'
data, sample_rates = sf.read(filename)
s_input = Signal(data, sample_rates)


while True :
    showMenu()
    lc = int(input('Nhap lua chon: '))
    if lc == 1:
      s_input.create_echo_effect(0.5, 0.5)
      data2, sample_rates2 = sf.read('output_echo.wav')
      s_out = Signal(data2, sample_rates2)
      signalPlot(s_input, s_out, 'echo')
    elif lc == 2:
      s_input.create_fade_in_out_effect(4.0, 4.0)
      data2, sample_rates2 = sf.read('output_fade.wav')
      s_out = Signal(data2, sample_rates2)
      signalPlot(s_input, s_out, 'fade in và fade out')
    elif lc == 3:
      s_input.create_modulation_effect(2.0, 1.0)
      data2, sample_rates2 = sf.read('output_modulation.wav')
      s_out = Signal(data2, sample_rates2)
      signalPlot(s_input, s_out, 'modulation')
    elif lc == 4:
      s_input.create_reverb_effect(0.05, 0.5, 1)
      data2, sample_rates2 = sf.read('output_reverb.wav')
      s_out = Signal(data2, sample_rates2)
      signalPlot(s_input, s_out, 'reverb')
    elif lc == 5:
      s_input.create_reversal_effect()
      data2, sample_rates2 = sf.read('output_reversal.wav')
      s_out = Signal(data2, sample_rates2)
      signalPlot(s_input, s_out, 'reversal')
    elif lc == 6:
      print("Chuong trinh da thoat")
      break

