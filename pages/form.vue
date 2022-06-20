<template>
  <div class="booking">
    <div class="overlay">
      <div v-if="!form" class="container">
        <div class="row justify-content-center">
          <div class="col-8">
            <div class="error-message" v-if="msg">
              <i class="fa fa-exclamation-triangle" aria-hidden="true" />
              <p>{{ msg }}</p>
            </div>
            <div class="error-message" v-else>
              <iframe  className='bookerIframe'
                src='https://dev.iclerk.io/scan2book/booker/4130a539143c4224b78cd6b0a436759a/e7bf47faa4fa1194/?iframe=true'
                height="708" :style="{ border: '0' , borderRadius: '25px' ,
              width: '500px' }" allowFullScreen="" loading="lazy" referrerPolicy="no-referrer-when-downgrade"></iframe>
            </div>
          </div>
        </div>
      </div>
      <div v-if="form" class="container">
        <div class="row">
          <div class="col-12">
            <div class="header">
              <loader v-if="$store.state.loader" />
            </div>
          </div>
        </div>
        <div class="row">
          <div class="col-md-12 col-lg-6 px-2 pl-lg-3 pb-4 pr-lg-0">
            <div class="booking-form rounded mt-md-5 mt-2">
              <form class="px-1 px-lg-3">
                <i v-if="$route.path == '/form/personal-info'" class="fa fa-arrow-circle-left" aria-hidden="true"
                  @click="back" />
                <nuxt-child />
                <div class="container fare-next px-0 pt-2">
                  <div class="row m-0">
                    <div class="col-md-6 col-12 px-0 ">
                      <div v-if="$route.name == 'form'">
                        <h4>Fare</h4>
                        <p v-if="$store.state.price" class="font-fare my-3">
                          <b>&#163;{{ $store.state.price }}</b>
                        </p>
                        <p v-else class="font-fare mb-1 my-3">
                          &#163;0.00
                        </p>
                        <i class="d-inline-block">EST</i>
                        <p v-if="$store.state.distance" class="d-inline-block">
                          <b>{{ $store.state.distance }} Miles</b>
                        </p>
                        <p v-else class="d-inline-block">
                          0 Miles
                        </p>
                      </div>
                    </div>
                    <div class="col-md-6 col-12 text-right">
                      <button class="standard-btn hover-effect mt-4 w-100 px-0" @click.prevent="next">
                        {{ btnText }}
                      </button>
                    </div>
                  </div>
                </div>
              </form>
            </div>
          </div>
          <div class="col-lg-6 mt-2 mt-lg-5 pl-lg-0 pb-4 form-features">
            <div v-if="this.$route.path =='/form/personal-info'" class="qouation rounded h-100 p-2 mx-3">
              <div class="stepper">
                <ul class="pl-3 pt-2">
                  <li>
                    <i class="fa points fa-map-marker" aria-hidden="true" />
                    <h3 class="d-inline-block">
                      From
                    </h3>
                    <div class="">
                      <p>{{ $store.state.pickup_address }}</p>
                    </div>
                  </li>
                  <li>
                    <i class="fa points fa-map-marker" aria-hidden="true" />
                    <h3 class="d-inline-block">
                      To
                    </h3>
                    <div>
                      <p>{{ $store.state.dropoff_address }}</p>
                    </div>
                  </li>
                  <li v-if="$store.state.via1_id || $store.state.via2_id || $store.state.via3_id">
                    <i class="fa points fa-map-marker" aria-hidden="true" />
                    <h3 class="d-inline-block">
                      Via
                    </h3>
                    <div>
                      <p class="mb-1">
                        {{ $store.state.via1_address }}
                      </p>
                      <p class="mb-1">
                        {{ $store.state.via2_address }}
                      </p>
                      <p class="mb-1">
                        {{ $store.state.via3_address }}
                      </p>
                    </div>
                  </li>
                  <li>
                    <i class="fa points fa-car" aria-hidden="true" />
                    <h3 class="d-inline-block">
                      Vehicle Type
                    </h3>
                    <div>
                      <p>{{ $store.state.vehicle_group }}</p>
                    </div>
                  </li>
                  <li>
                    <i class="fa  points fa-user" aria-hidden="true" />
                    <h3 class="d-inline-block">
                      Name
                    </h3>
                    <div>
                      <p class="">
                        {{ $store.state.name }}
                      </p>
                    </div>
                  </li>
                  <li>
                    <i class="fa  points fa-phone" aria-hidden="true" />
                    <h3 class="d-inline-block">
                      Phone
                    </h3>
                    <div>
                      <p class="">
                        {{ $store.state.phone }}
                      </p>
                    </div>
                  </li>
                  <li>
                    <i class="fa points fa-gbp" aria-hidden="true" />
                    <h3 class="d-inline-block">
                      Cost
                    </h3>
                    <div>
                      <p class="cost">
                        &#163;{{ $store.state.price }}
                      </p>
                    </div>
                  </li>
                </ul>
              </div>
              <!--                <h3 class="text-center">-->
              <!--                  Your Qoutation-->
              <!--                </h3>-->
              <!--                <ul class="pl-0">-->
              <!--                  <li>-->
              <!--                    <div class="unit">-->
              <!--                      <span>Journey Cost </span> <span>&#163;{{ $store.state.price }}</span>-->
              <!--                    </div>-->
              <!--                  </li>-->
              <!--                  <li>-->
              <!--                    <div class="unit">-->
              <!--                      <span>Pickup Address </span> <span>{{ $store.state.pickup_address }}</span>-->
              <!--                    </div>-->
              <!--                  </li>-->
              <!--                  <li><span>Dropoff Address </span> <span>{{ $store.state.dropoff_address }}</span></li>-->
              <!--                  <li><span>Phone </span><span> {{ $store.state.phone }}</span></li>-->
              <!--                  <li><span>Name </span><span> {{ $store.state.name }}</span></li>-->
              <!--                  <li><span>Passengers </span><span> {{ $store.state.passengers }}</span></li>-->
              <!--                </ul>-->
            </div>
            <section v-if="this.$route.path =='/form'" class="ml-0 ml-sm-4 right-from">
              <h4>Your Oldham Taxi Network</h4>
              <p class="mb-4">
                Booking a taxi has never been so easy!
              </p>
              <p class="mb-4">
                Enjoy an entirely new taxi experience with our web taxi booking system.
                The new web system makes it even more easier to book a taxi and gives you full control of your booking
                with a touch of your finger tips.
              </p>
              <div class="start-content">
                <img alt="logo" src="~assets/img/logo.png">
                <h4>Everything is backed by A2B Tommyfield Cars. Free cancelation, Track your driver, ETA, Quotations
                  and much more.</h4>
              </div>
            </section>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script type="text/javascript">
import Vue from 'vue'
import loader from '@/components/loader.vue'
export default {
  components: {
    loader
  },
  data() {
    return {
      form: null,
      msg: ""
    }
  },

  computed: {
    btnText() {
      if (this.$route.path === '/form/personal-info') {
        return 'Confirm Booking'
      } else {
        return 'NEXT'
      }
    }
  },
  destroyed() {
    clearTimeout(this.timeout)
    clearInterval(this.interval)
  },

  // updated() {
  //   const pickup = { lat: this.$store.state.pickupLat, lng: this.$store.state.pickupLng }
  //   const dropoff = { lat: this.$store.state.dropoffLat, lng: this.$store.state.dropoffLng }
  //   this.path.push(pickup)
  //   this.path.push(dropoff)
  // },
  mounted() {
    var self = this
    self.$store.commit('hide', true)
    self.timeout = setTimeout(function () {
      self.$store.commit('hide', false)
    }, 500)
    self.getForm()
    self.interval = setInterval(function () {
      self.getForm()
    }, 15000)
  },
  methods: {
    getForm() {
      var self = this
      Vue.axios.get('/show/')
        .then(function (response) {
          self.form = response.data[0].show
          self.msg = response.data[0].message
        })
    },
    back() {
      this.$router.go(-1)
      this.$store.commit('error', '')
    },
    next() {
      if (this.$route.path === '/form') {
        this.getQoute()
      } else {
        window.scrollTo(0, 0)
        this.book()
      }
    },
    home() {
      if (this.$route.path === '/') {
        window.location = '/'
      } else {
        this.$store.dispatch('resetState')
        this.$router.push({ path: '/' })
      }
    },
    getQoute() {
      if (!this.$store.state.droppoff_id ||
        !this.$store.state.pickup_id || !this.$store.state.vehicle_type || !this.$store.state.price) {
        this.$store.commit('error', 'Pleass fill the required fields')
      } else {
        this.$store.commit('error', '')
        this.$router.push({ path: 'form/personal-info' })
      }
    },
    viewDetails() {
      window.location = 'https://www.247radiocarz.co.uk/'
    },
    book() {
      window.scrollTo(0, 0)

      const self = this
      if (!self.$store.state.name) {
        self.$store.commit('error', 'Please enter valid name')
        self.timeout = setTimeout(function () {
          self.$store.commit('error', '')
        }, 3000)
      }
      if ((self.$store.state.phone.match(/[a-zA-Z]/g) || self.$store.state.phone.length < 9 || self.$store.state.phone.length > 13)) {
        self.$store.commit('error', 'Please enter valid phone number')
        self.timeout = setTimeout(function () {
          self.$store.commit('error', '')
        }, 3000)
      } else {
        if (this.$store.state.pickup_date) {
          self.$store.commit('loader', true)
          var data = {
            // TODO: Use mapState
            name: this.$store.state.name,
            pickup_ref: this.$store.state.pickup_id,
            passenger: this.$store.state.passengers,
            dropoff_ref: this.$store.state.droppoff_id,
            phone: this.$store.state.phone,
            notes: this.$store.state.notes,
            pickup_extra: '',
            pickup_date: this.$store.state.pickup_date,
            vehicle_type: this.$store.state.vehicle_type,
            vehicle_id: this.$store.state.vehicle_id,
            vehicle_group: this.$store.state.vehicle_group,
            vehicle_title: this.$store.state.vehicle_title
            // via1_ref: this.$store.state.via1_id,
            // via1_postcode: this.$store.state.via1_address,
            // via2_ref: this.$store.state.via2_id,
            // via2_postcode: this.$store.state.via2_address,
            // via3_ref: this.$store.state.via2_id,
            // via3_postcode: this.$store.state.via2_address,

          }
        } else {
          self.$store.commit('loader', true)
          data = {
            // TODO: Use mapState
            name: this.$store.state.name,
            pickup_ref: this.$store.state.pickup_id,
            passenger: this.$store.state.passengers,
            dropoff_ref: this.$store.state.droppoff_id,
            phone: this.$store.state.phone,
            notes: this.$store.state.notes,
            pickup_extra: '',
            vehicle_title: this.$store.state.vehicle_title,
            email: this.$store.state.email,
            vehicle_type: this.$store.state.vehicle_type,
            vehicle_group: this.$store.state.vehicle_group
            // via1_ref: this.$store.state.via1_id,
            // via1_postcode: this.$store.state.via1_address,
            // via2_ref: this.$store.state.via2_id,
            // via2_postcode: this.$store.state.via2_address,
            // via3_ref: this.$store.state.via2_id,
            // via3_postcode: this.$store.state.via2_address,

          }
        }

        Vue.axios.post('/booking/', data)
          .then(function (response) {
            self.$store.commit('loader', false)
            self.$store.commit('id', response.data.id)
            self.$store.commit('icabbi_status', response.data.icabbi_status)
            self.$store.commit('booking_status', response.data.booking_status)
            self.$router.push({ name: 'response' })
          })
          .catch(() => {
            self.$store.commit('loader', false)
            this.$router.push({ name: 'response' })
          })
      }
    }
  }
}
</script>
