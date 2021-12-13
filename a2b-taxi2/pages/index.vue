<template>
  <div class="titlepage-wrapper">
    <div class="hero-wrapper pt-lg-5 pt-0 ">
      <div class="layout" />
      <div class="container">
        <div class="row">
          <div class="col-xl-6" />
          <div class="col-xl-6">
            <div class="right pl-2 pl-sm-0" :class="{isload:isload}">
              <h1 class="premier">Premium Taxi Services</h1>
              <strong>in Oldham</strong>
              <p>Fast, Exemplary and Punctual</p>
              <button class="hover-effect" @click="booking">
                Book Now
              </button>
            </div>
          </div>
        </div>
        <!--        <div class="row hero-btns py-3 py-lg-5">-->
        <!--          <div class="col-12 text-center">-->
        <!--            <div class="">-->
        <!--              <button class=" mx-0 mx-lg-3 rounded">-->
        <!--                Book Online-->
        <!--              </button>-->
        <!--              <button class=" mx-0 mx-lg-3 rounded">-->
        <!--                Corporate Booking-->
        <!--              </button>-->
        <!--              <button class=" mx-0 mx-lg-3 rounded">-->
        <!--                Make Payment-->
        <!--              </button>-->
        <!--              <button class=" mx-0 mx-lg-3 rounded">-->
        <!--                Fare Guide-->
        <!--              </button>-->
        <!--            </div>-->
        <!--          </div>-->
        <!--        </div>-->
      </div>
    </div>
    <div class="features mt-5">
      <div class="container">
        <div class="row">
          <div class="col-12 col-lg-3 text-center mb-2">
            <img alt="airport" src="~assets/img/airport.png" class="mb-2">
            <h4 class="mb-2">
              Airport Transfer
            </h4>
            <p>
              A2B Tommyfield Cars provide a fast and friendly service to the airport at an affordable price. We travel to and from any
              airport around the country. We also have a range of vehicles from mini bus to prestige so you can now ride
              in comfort. Our service is 24 hours a day 7 days a week. Need that holiday? No problem we got you
            </p>
          </div>
          <div class="col-12 col-lg-3 text-center mb-2">
            <img alt="competitive price" src="~assets/img/compettive.png" class="mb-2">
            <h4 class="mb-2">
              Competitive Pricing
            </h4>
            <p>
              Looking for a cheap rate taxi? Sounds like you need to call us. A2B Tommyfield Cars are a well established firm with over
              30 years of experience around the Oldham and Manchester area. We offer a fixed fare service for long
              journeys so you know exactly how much you pay before you start your journey.
            </p>
          </div>
          <div class="col-12 col-lg-3 mb-2 text-center">
            <img alt="timely" src="~assets/img/timely.png" class="mb-2">
            <h4 class="mb-2">
              Timely & Safe
            </h4>
            <p>
              Get to places you want to travel to with us as we offer a prompt and punctual service in and around the
              Oldham area. Once booked our drivers will reach the pick up location in 3-4 minutes. You can also
              download our app. Book a taxi in seconds and see exactly where your car is and get an exact Eta.
            </p>
          </div>
          <div class="col-12 col-lg-3  mb-2 text-center">
            <img alt="service" src="~assets/img/best-services.png" class="mb-2">
            <h4 class="mb-2">
              Best Services
            </h4>
            <p>
              We strive to provide the best service around oldham. Our aim is to always be on time for our customers as
              getting late can cause alot of problems. We have cars scattered all around the oldham area so we can get
              cars to our customers within minutes.
            </p>
          </div>
        </div>
      </div>
    </div>
    <div class="mobile-app pt-1 mt-5 pb-2 pb-lg-0">
      <div class="container">
        <div class="row">
          <div class="col-md-4  d-none d-lg-block">
            <div class="wrapper-mobile">
              <img alt="mobile" src="~assets/img/mobile.png">
              <img alt="mobile car" src="~assets/img/mobile-car.png">
              <div class="text">
                <i>More better</i>
                <h4>
                  More Easy
                </h4>
              </div>
            </div>
          </div>
          <div class="col-md-8">
            <div class="right mt-lg-5 mt-2">
              <h4>
                Download the App
              </h4>
              <p>
                Want to save time and money? Just simply download our app today. Its easy to use and is available
                to download for free on Play store.
              </p>
              <div class="app-icons>">
                <a href="https://play.google.com/store/apps/details?id=com.icabbi.a2btommyfieldcars&hl=en"><img alt="play store" src="~assets/img/googleplay-store-btn.png"></a>
                <img alt="app store" class="d-none" src="~assets/img/appstore-btn.png">
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="title-aboutus mt-5 pt-0 pt-lg-5">
      <div class="container">
        <div class="row">
          <div class="col-md-6">
            <div class="left mb-2">
              <h4>About</h4>
              <h1 class="theme-clr">
                A2B Tommyfield Cars
              </h1>
              <p>
                Welcome to A2B Tommyfield Cars where our customers benefit from over 100 vehicles that are available to
                transport you 24/7 anywhere in the UK. We have introduced an affordable fare for our customers and ever
                since been rewarded with many loyal customers. We can provide a vehicle to suit any journey. Our large
                fleet allows us to supply prestige & executive vehicles for special occasions to standard cars that will
                get you from A to B. We also have a range of Airport taxis to take you from or to any airport in the UK.
              </p>
              <button class="standard-btn hover-effect">
                Learn More
              </button>
            </div>
          </div>
          <div class="col-md-6">
            <h4>About</h4>
            <h2 class="theme-clr">
              Our Services
            </h2>
            <ul>
              <li>
                <i class="fa fa-check" aria-hidden="true" />
                100% Customer-Satisfaction
              </li>
              <li>
                <i class="fa fa-check" aria-hidden="true" />
                No Hidden Charges, No Extra Costs
              </li>
              <li>
                <i class="fa fa-check" aria-hidden="true" />
                Fixed Prices
              </li>
              <li>
                <i class="fa fa-check" aria-hidden="true" />
                Fast & Safe Airport Transfers
              </li>
              <li>
                <i class="fa fa-check" aria-hidden="true" />
                Nationwide
              </li>
              <li>
                <i class="fa fa-check" aria-hidden="true" />
                Secure Online & App Booking
              </li>
              <button class="standard-btn hover-effect">
                Learn More
              </button>
            </ul>
          </div>
        </div>
      </div>
    </div>
    <div class="testemonial text-center">
      <div class="main-content">
        <h5>Client</h5>
        <h3 class="theme-clr">
          Testimonial
        </h3>
      </div>
      <div id="carouselExampleIndicators" class="carousel slide" data-ride="carousel" data-interval="5000">
        <ol class="carousel-indicators">
          <li data-target="#carouselExampleIndicators" data-slide-to="0" class="active" />
          <li data-target="#carouselExampleIndicators" data-slide-to="1" />
          <li data-target="#carouselExampleIndicators" data-slide-to="2" />
        </ol>
        <div class="carousel-inner">
          <div class="carousel-item active">
            <div class="container">
              <div class="row">
                <div class="col-md-12">
                  <div class="content">
                    <div class="review text-left">
                      <span class="qoute"><i class="fa fa-quote-right" aria-hidden="true" /></span>
                      <h3 class="remarks">
                        VERY GOOD TAXI SERVICE
                      </h3>
                      <p>
                        Very good taxi service, always on time and the staff are really nice and easy to talk to.
                        will definitely use them again and I recommend that everybody else does too. BEST TAXI SERVICE IN OLDHAM!!!!!!
                      </p>
                      <div class="client-info">
                        <div class="dp-cover">
                          <img alt="dp female" src="~assets/img/client-dp-female.png">
                        </div>
                        <div class="rating">
                          <span>Emma wilson</span><span>-</span>
                          <span>Customer</span>
                          <span>              <i class="fa fa-star" aria-hidden="true" />
                            <i class="fa fa-star" aria-hidden="true" />
                            <i class="fa fa-star" aria-hidden="true" />
                            <i class="fa fa-star" aria-hidden="true" /></span>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="carousel-item ">
            <div class="container">
              <div class="row">
                <div class="col-md-12">
                  <div class="content">
                    <div class="review text-left">
                      <span class="qoute"><i class="fa fa-quote-right" aria-hidden="true" /></span>
                      <h3 class="remarks">
                        BRILLIANT SERVICES
                      </h3>
                      <p>
                        I absolutely LOVE A2B Taxis, they never fail to let me down and are always there when I
                        need them! They're FAB! Great prices and a brilliant service!
                      </p>
                      <div class="client-info">
                        <div class="dp-cover">
                          <img alt="dp female" src="~assets/img/client-dp-female.png">
                        </div>
                        <div class="rating">
                          <span>Emily Jayne</span><span>-</span>
                          <span>Customer</span>
                          <span>
                            <i class="fa fa-star" aria-hidden="true" />
                            <i class="fa fa-star" aria-hidden="true" />
                            <i class="fa fa-star" aria-hidden="true" />
                            <i class="fa fa-star" aria-hidden="true" />
                            <i class="fa fa-star" aria-hidden="true" />
                          </span>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="carousel-item">
            <div class="container">
              <div class="row">
                <div class="col-md-12">
                  <div class="content">
                    <div class="review text-left">
                      <span class="qoute"><i class="fa fa-quote-right" aria-hidden="true" /></span>
                      <h3 class="remarks">
                        ALL PERFECT!
                      </h3>
                      <p>
                        Cheap prices quick driving freshie drivers all perfect
                      </p>
                      <div class="client-info">
                        <div class="dp-cover">
                          <img alt="dp male" src="~assets/img/client-dp-male.png">
                        </div>
                        <div class="rating">
                          <span>Graciano Luvunga</span><span>-</span>
                          <span>Customer</span>
                          <span>              <i class="fa fa-star" aria-hidden="true" />
                            <i class="fa fa-star" aria-hidden="true" />
                            <i class="fa fa-star" aria-hidden="true" />
                            <i class="fa fa-star" aria-hidden="true" /></span>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
        <a class="carousel-control-prev" href="#carouselExampleIndicators" role="button" data-slide="prev">
          <span class="carousel-control-prev-icon" aria-hidden="true" />
          <span class="sr-only">Previous</span>
        </a>
        <a class="carousel-control-next" href="#carouselExampleIndicators" role="button" data-slide="next">
          <span class="carousel-control-next-icon" aria-hidden="true" />
          <span class="sr-only">Next</span>
        </a>
      </div>
    </div>
    <div class="call-agent">
      <div class="container">
        <div class="row">
          <div class="col-12">
            <h5>Call us to book a taxi</h5>
            <h1>0161 213 1111</h1>
            <h5>The operator will call back immediately and report the cost of travel</h5>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script type="text/javascript">
export default {
  data() {
    return {
      isload: false
    }
  },
  mounted() {
    const self = this
    self.$store.dispatch('resetState')
    self.$store.commit('hide', true)
    setTimeout(function () {
      self.$store.commit('hide', false)
    }, 500)
    self.timeout = setTimeout(function () {
      self.isload = true
    }, 400)
  },

  destroyed() {
    this.$store.commit('hide', false)
    clearTimeout(this.timeout)
  },

  methods: {
    booking() {
      this.$router.push({ path: '/form' })
    },
    goHome() {
      this.$router.push({ path: '/' })
    }
  }
}
</script>
