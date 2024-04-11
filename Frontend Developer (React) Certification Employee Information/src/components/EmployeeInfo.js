import React from 'react';

class EmployeeInfo extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      employees: this.props.employees,
      searchTerm: '',
      selectedCountry: '',
      selectedLanguage: ''
    };
    this.filterMethod = this.filterMethod.bind(this);
    this.handleCountryChange = this.handleCountryChange.bind(this);
    this.handleLanguageChange = this.handleLanguageChange.bind(this);
  }
 
  filterMethod(e) { 
    this.setState({
      searchTerm: e.target.value.toLowerCase()
    })
  }

  handleCountryChange(e) {
    this.setState({
      selectedCountry: e.target.value
    });
    if (this.props.onCountryChange) {
      this.props.onCountryChange(e.target.value);
    }
  }

  handleLanguageChange(e) {
    this.setState({
      selectedLanguage: e.target.value
    });
    if (this.props.onLanguageChange) {
      this.props.onLanguageChange(e.target.value);
    }
  }

  render() {
    const { labelText } = this.props;
    const countryOptions = [
      { label: 'USA', value: 'USA' },
      { label: 'Germany', value: 'Germany' },
      { label: 'France', value: 'France' },
      { label: 'Canada', value: 'Canada' },
      { label: 'India', value: 'India' },
      { label: 'Poland', value: 'Poland' },
      { label: 'Japan', value: 'Japan' },
      { label: 'Spain', value: 'Spain' },
      { label: 'Australia', value: 'Australia' }
    ];
    const languageOptions = [
      { label: 'English', value: 'English' },
      { label: 'Spanish', value: 'Spanish' },
      { label: 'French', value: 'French' },
      { label: 'German', value: 'German' }
    ];
    return (
      <React.Fragment>
        <div className="controls">
          <select value={this.state.selectedCountry} onChange={this.handleCountryChange} {...this.props.countryProps}>
            <option value="">{labelText || 'Select Country'}</option>
            {countryOptions && countryOptions.map(option => (
              <option key={option.value} value={option.value}>{option.label}</option>
            ))}
          </select>
          <select value={this.state.selectedLanguage} onChange={this.handleLanguageChange}>
            <option value="">Select Language</option>
            {languageOptions && languageOptions.map(option => (
              <option key={option.value} value={option.value}>{option.label}</option>
            ))}
          </select>
        </div>
        Final Selections:
        <div>
          Country Selected: {this.state.selectedCountry}
        </div>
        <div>
          Language Selected: {this.state.selectedLanguage}
        </div>
      </React.Fragment>
    );
  }
}

export default EmployeeInfo;
