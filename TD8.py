from struct import *




def separate_data(data,low = False,interpolate=False):
    Ll = []
    Lr = []
    len_ = unpack('I',data[40:44])[0]
    for i in range(len_//4):
        L = unpack("hh",data[44+4*i:44+4*i+4])
        if interpolate and i>0:
            Ll.append((L[0]+Ll[i-1])//2)
            Lr.append((L[1]+Lr[i-1])//2)
        Ll.append(L[0])
        Lr.append(L[1])
        if low and i%2==0:
            Lr.pop()
            Ll.pop()

    return Ll,Lr



def create_dataframe(Ll, Lr):
    # create header

    Ltot = []
    for i in range(len(Ll)):
        Ltot.append(Ll[i])
        Ltot.append(Lr[i])
    str_ = ""
    for i in range(len(Ltot)):
        str_ += "h"
    data2 = pack(str_, *Ltot)
    return data2


# -------------------------------------------------
# Exercice 2 - Write stereo audio data to a WAV file
# -------------------------------------------------
def write_file(left, right, filename,low=False,interpolate=False,factor = 1):
    fc = factor
    a = 1
    if low:
        a = 1/2
    if interpolate:
        a = 2
    """
    Writes a stereo WAV file from left and right audio channels.
    """
    with open(filename, "wb") as f:
        f.write(b"RIFF")  # Start of RIFF header
        f.write(pack("I", 44 - 8 + len(left) * 4))  # Total file size minus "RIFF" and size field

        f.write(b"WAVEfmt ")  # Format chunk marker
        # Format chunk: PCM, 2 channels, 44100Hz, 16-bit samples
        f.write(pack("IHHIIHH", 16, 1, 2, fc*a*44100, fc*a*44100 * 4, 4, 16))
        f.write(b"data")  # Start of data chunk
        f.write(pack("I", len(left) * 4))  # Data size in bytes
        f.write(create_dataframe(left,right))
        """
        16 : size of 'fmt ' chunk
        1  : PCM format
        2  : number of channels (stereo)
        44100 : sample rate
        44100 * 4 : byte rate = sample_rate * num_channels * bytes_per_sample
        4 : block align = num_channels * bytes_per_sample
        16 : bits per sample
        """
filename = "the_wall.wav"
f = open(filename, "rb")
data = f.read()
low, interpolate = False, False
Ll, Lr = separate_data(data,low,interpolate)

write_file(Ll,Lr,"my_filelow_interpolateFAST.wav",low,interpolate,5)



filename = "my_filelow_interpolate2.wav"
f = open(filename, "rb")
data2 = f.read()



print(data[:90])
print(data2[:90])