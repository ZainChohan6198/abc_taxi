<template>
  <div class="form-content pt-2">
    <div class="d-block d-md-flex">
      <div class="input-group mb-2 mr-sm-2 ">
        <div class="input-group-prepend">
          <div class="input-group-text">
           Name:
          </div>
        </div>

        <input v-model="name" type="text" class="form-control" placeholder="Enter your name">

<!--        <div v-if="this.$store.state.error && !this.$store.state.name" class="error-badge" role="alert">-->
<!--          <b>Please Enter Name</b>-->
<!--        </div>-->
      </div>
      <div class="input-group mb-2 ">
        <div class="input-group-prepend">
          <div class="input-group-text">
            Phone:
          </div>
        </div>
        <input v-model="phone" type="text" class="form-control" placeholder="Enter your phone">
        <div
          v-if="$store.state.error &&
            ($store.state.phone.match(/[a-zA-Z]/g) || $store.state.phone.length < 9 || $store.state.phone.length > 13)"
          class="error-badge"
          role="alert"
        >
          <b>Please enter valid phone number</b>
        </div>
      </div>
    </div>

    <div class="input-group mt-2 mb-4 mr-sm-2">
      <div class="input-group-prepend">
        <div class="input-group-text">
          Email:
        </div>
      </div>
      <input v-model="email" type="email" class="form-control" placeholder="Enter your email">
    </div>

    <h4 class="mb-1">
      Pickup Date & Time
    </h4>
    <div class="input-group date mb-3 mr-sm-2">
      <div class="input-group-prepend">
        <div class="input-group-text">
          <i class="fa fa-calendar" aria-hidden="true" />
        </div>
      </div>
      <datetime
        v-model="pickup_date"
        :min-datetime="date | moment('YYYY-MM-DDTHH:mm:ss')"
        :placeholder="date | moment('MMM DD ,gggg, h:mma')"
        type="datetime"
        class="text-left"
      />
    </div>
    <h4>Notes to driver</h4>
    <textarea class="w-100" v-model="notes" placeholder="Leave notes..." rows="9" />
    <div class="btn-container d-flex mt-5">
      <h4 class="mr-2">Payment Mehtods</h4>
      <select>
        <option>Cash</option>
      </select>
    </div>
  </div>
</template>
<script type="text/javascript">
export default {
  scrollToTop: true,
  data() {
    return {
      date: new Date(),
      select: 'Select date & time'
    }
  },
  computed: {
    phone: {
      get() {
        return this.$store.state.phone
      },
      set(phone) {
        this.$store.commit('phone', phone)
      }
    },
    name: {
      get() {
        return this.$store.state.name
      },
      set(name) {
        this.$store.commit('name', name)
      }
    },
    email: {
      get() {
        return this.$store.state.email
      },
      set(email) {
        return this.$store.commit('email', email)
      }
    },
    journey_type: {
      get() {
        return this.$store.state.journey_type
      },
      set(journey_type) {
        return this.$store.commit('journey_type', journey_type)
      }
    },

    notes: {
      get() {
        return this.$store.state.notes
      },
      set(notes) {
        return this.$store.commit('notes', notes)
      }
    },
    return_date: {
      get() {
        return this.$store.state.return_date
      },
      set(return_date) {
        return this.$store.commit('return_date', return_date)
      }
    },
    pickup_date: {
      get() {
        return this.$store.state.pickup_date
      },
      set(pickup_date) {
        return this.$store.commit('pickup_date', pickup_date)
      }
    },
    checked: {
      get() {
        return this.$store.state.checked
      },
      set(checked) {
        this.$store.commit('checked', checked)
        if (checked) {
          var fare = this.$store.state.price * 2
          this.$store.commit('price', fare)
        } else { fare = this.$store.state.price / 2 }
        this.$store.commit('price', fare)
      }
    }
  },
  // mounted() {
  //   const self = this
  //   if (!self.$store.state.droppoff_id) {
  //     self.$router.push({ path: '/' })
  //   }
  // }
}
</script>
