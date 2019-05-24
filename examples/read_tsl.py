import tsl2591

if __name__ == '__main__':

    tsl = Tsl2591()  # initialize
    # read raw values (full spectrum and ir spectrum)
    full, ir = tsl.get_full_luminosity()
    lux = tsl.calculate_lux(full, ir)  # convert raw values to lux
    tsl.set_gain(GAIN_MED)
    tsl.set_timing(INTEGRATIONTIME_300MS)
    output = {
        "lux": lux,
        "full": full,
        "ir": ir,
        "gain": tsl.get_gain(),
        "integration_time": tsl.get_timing()
    }

    while True:
        print(output)
        time.sleep(2)

    def test(int_time=INTEGRATIONTIME_100MS, gain=GAIN_LOW):
        tsl.set_gain(gain)
        tsl.set_timing(int_time)
        full_test, ir_test = tsl.get_full_luminosity()
        lux_test = tsl.calculate_lux(full_test, ir_test)
        print('Lux = %f  full = %i  ir = %i' % (lux_test, full_test, ir_test))
        print("integration time = %i" % tsl.get_timing())
        print("gain = %i \n" % tsl.get_gain())

    for i in [INTEGRATIONTIME_100MS,
              INTEGRATIONTIME_200MS,
              INTEGRATIONTIME_300MS,
              INTEGRATIONTIME_400MS,
              INTEGRATIONTIME_500MS,
              INTEGRATIONTIME_600MS]:
        test(i, GAIN_LOW)

    for i in [GAIN_LOW,
              GAIN_MED,
              GAIN_HIGH,
              GAIN_MAX]:
        test(INTEGRATIONTIME_100MS, i)
