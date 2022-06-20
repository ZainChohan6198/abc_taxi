<template>
  <div id="support" class="titlepage-wrapper">
    <div class="container title-aboutus">
      <div class="row mt-3 mb-5">
        <div class="col-12 text-center">
          <h4 class="theme-clr mb-3">
            Support
          </h4>
          <div class="bg-light rounded">
            <p class="text-center">
              If you have a question or issue  relating to your booking or need support then please submit an enquiry below.
              Our member of the Customer Service team will be  investigating and get back to you as soon as possible.
            </p>
            <button class="standard-btn hover-effect" @click="touch">
              GET IN TOUCH
            </button>
          </div>
        </div>
      </div>
      <div class="row mt-3 mb-5">
        <div class="col-12 text-center">
          <h4 class="theme-clr">
            FAQs
          </h4>
        </div>
      </div>
      <div class="row mt-3">
        <div class="col-md-6 col-12">
          <div class="question">
            <div class="heading d-flex">
              <i class="fa fa-question-circle mr-2 pt-1" aria-hidden="true" />
              <h5 class="theme-clr">
                How do i cancel my booking?
              </h5>
            </div>
            <div class="question-data">
              <p>
                Simply call our office number 0161 213 1111 and it will give you an option on the automated system to
                cancel your taxi. You will have to confirm you wish to cancel twice and the booking will be cancelled.
              </p>
            </div>
          </div>
        </div>
        <div class="col-md-6 col-12">
          <div class="question">
            <div class="heading d-flex">
              <i class="fa fa-question-circle mr-2 pt-1" aria-hidden="true" />
              <h5 class="theme-clr">
                How do i get a fixed fare?
              </h5>
            </div>
            <div class="question-data">
              <p> Contact our office on 0161 213 1111 and one of our operators will give you the best fixed fare we can offer you.</p>
            </div>
          </div>
        </div>
      </div>
      <div class="row mt-3">
        <div class="col-md-6 col-12">
          <div class="question">
            <div class="heading d-flex">
              <i class="fa fa-question-circle mr-2 pt-1" aria-hidden="true" />
              <h5 class="theme-clr">
                Can we pay by card?
              </h5>
            </div>
            <div class="question-data">
              <p> Unfortunatly we dont have this facility but will do in the near future.</p>
            </div>
          </div>
        </div>
        <div class="col-md-6 col-12">
          <div class="question">
            <div class="heading d-flex">
              <i class="fa fa-question-circle mr-2 pt-1" aria-hidden="true" />
              <h5 class="theme-clr">
                Do you have an app?
              </h5>
            </div>
            <div class="question-data">
              <p> Yes we have an app booking system which you can download today, for free.</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  mounted() {
    const self = this
    self.$store.dispatch('resetState')
    self.$store.commit('hide', true)
    this.time = setTimeout(function () {
      self.$store.commit('hide', false)
    }, 500)
  },
  destroyed() {
    clearTimeout(this.timeout)
    this.$store.commit('hide', false)
  },
  methods: {
    touch() {
      this.$router.push({ path: '/Contactus' })
    }
  }
}
</script>
