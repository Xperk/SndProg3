import soundfile as sf
import numpy as np
from scipy.signal import lfilter

class Signal:
    def __init__(self, data, sample_rates):
        self.data = data
        self.sample_rates = sample_rates
        self.root = self.data[0];
        self.length = len(self.data)

    # Tạo file có hiệu ứng echo từ file input.wav
    def create_echo_effect(self, e_delay, e_decay):
      # Tính toán thời gian trễ và mức độ phản hồi của hiệu ứng echo
      delay_sec = e_delay
      decay = e_decay
    
      # Tính toán số lượng mẫu tương ứng với thời gian trễ
      delay_samples = int(delay_sec * self.sample_rates)
    
      # Tạo một bộ đệm mới và sao chép các mẫu âm thanh vào bộ đệm này
      new_data = np.zeros_like(self.data)
      new_data[:delay_samples] = self.data[:delay_samples]
    
      # Tính toán các mẫu mới của hiệu ứng echo và thêm chúng vào bộ đệm
      for i in range(delay_samples, len(self.data)):
        new_data[i] = self.data[i] + decay * new_data[i - delay_samples]
    
      # Ghi bộ đệm đã được xử lý vào file mới bằng hàm write của thư viện soundfile
      sf.write('output_echo.wav', new_data, self.sample_rates)
    
    
    #Tạo hiệu ứng fade in fade out
    def create_fade_in_out_effect(self, in_duration, out_duration):
      # Tính toán thời gian của fade in và fade out
      fade_in_duration = in_duration
      fade_out_duration = out_duration
    
      # Tính toán số lượng mẫu tương ứng với fade in fade out
      fade_in_samples = int(fade_in_duration * self.sample_rates)
      fade_out_samples = int(fade_out_duration * self.sample_rates)
    
      # Tạo dãy dốc đơn vị tương ứng với hiệu ứng
      fade_in_shape = np.linspace(0.0, 1.0, fade_in_samples, False)
      fade_out_shape = np.linspace(1.0, 0.0, fade_out_samples, False)
    
      # Áp dụng fade in và fade out
      self.data[:fade_in_samples, :] = np.multiply(self.data[:fade_in_samples, :],
                                              fade_in_shape.reshape(-1, 1))
      self.data[-fade_out_samples:, :] = np.multiply(self.data[-fade_out_samples:, :],
                                                fade_out_shape.reshape(-1, 1))
    
      # Ghi âm thanh được xử lý vào file mới
      output_filename = 'output_fade.wav'
      sf.write(output_filename, self.data, self.sample_rates)
    
    
    #Tạo hiệu ứng âm thanh reverb
    def create_reverb_effect(self, delay, decay, wet):
      # Tính toán số mẫu tương ứng với thời gian delay
      delay_samples = int(delay * self.sample_rates)
    
      # Tính toán hệ số alpha cho bộ lọc FIR
      alpha = np.sqrt(decay)
    
      # Tạo impulse response cho bộ lọc FIR
      ir = np.zeros(delay_samples + 1)
      ir[0] = 1.0
      ir[delay_samples] = alpha
    
      # Áp dụng hàm lfilter() để áp dụng bộ lọc FIR
      # trên tín hiệu âm thanh đầu vào
      filtered = lfilter(ir, [1.0, -alpha], self.data, axis=0)
    
      # Tính toán tín hiệu wet và tín hiệu dry
      wet_signal = wet * filtered
      dry_signal = (1 - wet) * self.data
    
      # Tổng hợp tín hiệu wet và tín hiệu dry để tạo hiệu ứng reverb
      output = wet_signal + dry_signal
      # Ghi ra file âm thanh đầu ra
      output_filename = 'output_reverb.wav'
      sf.write(output_filename, output, self.sample_rates)
    
    
    #Tạo hiệu ứng âm thanh modulation
    def create_modulation_effect(self, m_freq, m_depth):
      # thiết lập các thông số của tín hiệu modulation
      freq = m_freq  # tần số của tín hiệu modulation
      depth = m_depth  # độ sâu của modulation
    
      # tạo tín hiệu modulation
      modulation = (
        1 + depth * np.cos(2 * np.pi * freq * np.arange(len(self.data)) / self.sample_rates))
    
      modulation = np.resize(modulation, self.data.shape)
    
      # tính tín hiệu modulated
      modulated_signal = self.data * modulation
    
      # ghi file âm thanh mới
      filename = 'output_modulation.wav'
      sf.write(filename, modulated_signal, self.sample_rates)
    
    
    #Tạo hiệu ứng âm thanh reversal
    def create_reversal_effect(self):
      # Lật ngược mảng
      reversed_data = np.flipud(self.data)
      # Ghi file âm thanh mới
    
      filename = 'output_reversal.wav'
      sf.write(filename, reversed_data, self.sample_rates)